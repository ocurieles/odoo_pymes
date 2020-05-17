# -*- coding: utf-8 -*-
# from odoo import http


# class PymesCustom(http.Controller):
#     @http.route('/pymes_custom/pymes_custom/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/pymes_custom/pymes_custom/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('pymes_custom.listing', {
#             'root': '/pymes_custom/pymes_custom',
#             'objects': http.request.env['pymes_custom.pymes_custom'].search([]),
#         })

#     @http.route('/pymes_custom/pymes_custom/objects/<model("pymes_custom.pymes_custom"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('pymes_custom.object', {
#             'object': obj
#         })
