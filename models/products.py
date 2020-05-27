from odoo import fields, models, api, _
from odoo.exceptions import AccessError, UserError, ValidationError


class Products(models.Model):
    _inherit = 'product.template'

    actual_user = fields.Integer('actual_user', compute='_get_actual_user', store=False)
    self_delivery = fields.Boolean('isSelfDelivery', default=False)

    @api.depends_context('user')
    def _get_actual_user(self):
        self.actual_user = self.env.user.tag_ids.id
        print(self.env.user.tag_ids.id)

    @api.model
    def create(self, vals):
        if vals['list_price'] == 1.0:
            raise UserError(_('You need set the Price'))

        vals['tag_ids'] = self.env.user.tag_ids

        result = super(Products, self).create(vals)
        result.create_first_supplier_info()
        return result

    @api.model
    def update_supplier_info(self):
        products = self.env['product.template'].search([('is_published', '=', True)])

        for product in products:
            supplier_info = self.env['product.supplierinfo'].sudo().search([
                ('product_tmpl_id.id', '=', product.id)
            ])

            if not supplier_info:
                self.create_supplier_info(product)

        return

    def update_stock(self):
        default_product_id = len(self.product_variant_ids) == 1 and self.product_variant_id.id
        action = self.env.ref('stock.action_change_product_quantity').read()[0]
        action['context'] = dict(
            self.env.context,
            default_product_id=default_product_id,
            default_product_tmpl_id=self.id
        )
        return action

    def create_first_supplier_info(self):
        res = self.env['product.supplierinfo']

        # create a supplier_info
        self.env['product.supplierinfo'].create({
            'name': self.env.user.partner_id.id,
            'product_tmpl_id': self.id,
            'price': self.list_price,
            'currency_id': self.currency_id.id,
            'min_qty': 1,
            'delay': 1
        })

    def create_supplier_info(self, product):
        res = self.env['product.supplierinfo']

        # create a supplier_info
        product.env['product.supplierinfo'].create({
            'name': self.env.user.partner_id.id,
            'product_tmpl_id': product.id,
            'price': product.list_price,
            'currency_id': product.currency_id.id,
            'min_qty': 1,
            'delay': 1
        })

