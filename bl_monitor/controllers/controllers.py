# -*- coding: utf-8 -*-
# from odoo import http


# class BlMonitor(http.Controller):
#     @http.route('/bl_monitor/bl_monitor/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/bl_monitor/bl_monitor/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('bl_monitor.listing', {
#             'root': '/bl_monitor/bl_monitor',
#             'objects': http.request.env['bl_monitor.bl_monitor'].search([]),
#         })

#     @http.route('/bl_monitor/bl_monitor/objects/<model("bl_monitor.bl_monitor"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('bl_monitor.object', {
#             'object': obj
#         })
