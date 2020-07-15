from odoo import fields, models, api


class SaleOrder (models.Model):
    _inherit = 'sale.order'

    def _action_confirm(self):
        res = super(SaleOrder, self).action_confirm()
        for rec in self:
            2







    


