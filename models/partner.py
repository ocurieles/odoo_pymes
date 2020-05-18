# -*- coding: utf-8 -*-

from odoo import api, fields, models


class PymesPartner(models.Model):
    _inherit = 'res.partner'

    bank_id = fields.Many2one('res.bank', string='Bank')
    account_id = fields.Many2one('res.partner.bank', string='Bank Account')







