from odoo import fields, models, api


class User(models.Model):
    _inherit = 'res.users'

    tag_ids = fields.Many2many('product.tag', string='Tag Pyme')
