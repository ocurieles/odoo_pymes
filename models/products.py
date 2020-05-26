from odoo import fields, models, api
from odoo.addons.product.models.product import SupplierInfo


class Products (models.Model):
    _inherit = 'product.template'

    actual_user = fields.Integer('actual_user', compute='_get_actual_user', store=False)
    self_delivery = fields.Boolean('isSelfDelivery', default=False)

    @api.depends_context('user')
    def _get_actual_user(self):
        self.actual_user = self.env.user.tag_ids.id
        print(self.env.user.tag_ids.id)

    @api.model
    def create(self, vals):
        vals['tag_ids'] = self.env.user.tag_ids

        result = super(Products, self).create(vals)
        result.create_supplier_info()
        return result

    def create_supplier_info(self):
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




    '''@api.model
    def create_partner_related(self):
        products = self.env['product.template'].search(self)
        for product in products:
            data = SupplierInfo.create({'name': self.create_uid.partner_id,'product_tmpl_id': product.id, 'min_quantity':1,
                                        'price': product.price})
                                        '''
