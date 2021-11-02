# -*- coding: utf-8 -*-

from odoo import models, fields, api


class bl_monitor(models.Model):
    _name = "bl_monitor.bl_monitor"
    _description = "bl_monitor.bl_monitor"

    name = fields.Char()
    value = fields.Integer()
    value2 = fields.Float(compute="_value_pc", store=True)
    description = fields.Text()

    @api.depends("value")
    def _value_pc(self):
        for record in self:
            record.value2 = float(record.value) / 100


class StockPickingInherit(models.Model):
    _inherit = "stock.picking"
    valeur = fields.Char(string="valeur ici")
    def rien(self):
        pass