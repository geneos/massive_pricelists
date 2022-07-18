# -*- coding: utf-8 -*-
# from odoo import http


# class MassivePricelists(http.Controller):
#     @http.route('/massive_pricelists/massive_pricelists/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/massive_pricelists/massive_pricelists/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('massive_pricelists.listing', {
#             'root': '/massive_pricelists/massive_pricelists',
#             'objects': http.request.env['massive_pricelists.massive_pricelists'].search([]),
#         })

#     @http.route('/massive_pricelists/massive_pricelists/objects/<model("massive_pricelists.massive_pricelists"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('massive_pricelists.object', {
#             'object': obj
#         })
