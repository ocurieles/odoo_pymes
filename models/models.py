# -*- coding: utf-8 -*-

# from odoo import models, fields, api


# class pymes_custom(models.Model):
#     _name = 'pymes_custom.pymes_custom'
#     _description = 'pymes_custom.pymes_custom'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100
