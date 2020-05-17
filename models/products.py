from odoo import fields, models, api


class Products (models.Model):
    _inherit = 'product.template'

    actual_user = fields.Integer('actual_user', compute='_get_actual_user', store=False)

    @api.depends_context('user')
    def _get_actual_user(self):
        self.actual_user = self.env.user.tag_ids.id
        print(self.env.user.tag_ids.id)

    @api.model
    def create(self, vals):

        vals['tag_ids'] = self.env.user.tag_ids

        result = super(Products, self).create(vals)
        return result












    


