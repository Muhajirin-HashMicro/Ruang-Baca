# -*- coding: utf-8 -*-
# from odoo import http


# class Ruangbuku(http.Controller):
#     @http.route('/ruangbuku/ruangbuku/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/ruangbuku/ruangbuku/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('ruangbuku.listing', {
#             'root': '/ruangbuku/ruangbuku',
#             'objects': http.request.env['ruangbuku.ruangbuku'].search([]),
#         })

#     @http.route('/ruangbuku/ruangbuku/objects/<model("ruangbuku.ruangbuku"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('ruangbuku.object', {
#             'object': obj
#         })
