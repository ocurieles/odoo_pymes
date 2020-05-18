from odoo import fields, models, api


class ModelName (models.Model):
    _inherit = 'res.partner.bank'

    account_type = fields.Selection([
        ('cheking', 'Checking Account'),
        ('saving', 'Saving Account')])
    


