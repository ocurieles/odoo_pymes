# -*- coding: utf-8 -*-

from odoo import api, fields, models


class Partner(models.Model):
    _inherit = 'res.partner'

    company_specs = name = fields.Char()

