# -*- coding:utf-8 -*-
from odoo import api, fields, models 


class StockPickingInherit(models.Model):
    _inherit = "stock.picking"

    custom_state = fields.Selection(
        string='Statut',
        selection=[('encours', 'En Cours'),
                   ('pret', 'Pret'),
                   ('livre', 'Livré')],
        default="encours" )

    state_paye = fields.Boolean(
        string='Statut Payement', default=False,
        required=False)

    def action_pret(self):
        if self.custom_state != 'livre':
            self.write({'custom_state':'pret'})

    def action_livre(self):
        self.write({'custom_state':'livre'})