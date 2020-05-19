# -*- coding: utf-8 -*-

from odoo import api, fields, models


class Partner(models.Model):
    _inherit = 'res.partner'

    company_specs = name = fields.Char()

    def go_website(self):
        website = self.env['website'].search([
            ('id', '=', 1), ])
        website._force()
        return {
            'type': 'ir.actions.act_url',
            'url': '/',
            'target': 'self',
        }

