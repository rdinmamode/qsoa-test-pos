# -*- coding:utf-8 -*-

from odoo import fields, models, api
from odoo.tools import float_compare, float_is_zero

class PosOrderInherit(models.Model):
    _inherit = "pos.order"
    
    vali = fields.Boolean(
        string='Vali', 
        required=False)
    
    # @api.model
    # def create_from_ui(self, orders, draft=False):
    #     order_ids = super(PosOrderInherit, self).create_from_ui(orders, draft)
    #     for order in self.sudo().browse([o['id'] for o in order_ids]):
    #         for line in order.lines.filtered(lambda
    #                                                  l: l.product_id == order.config_id.down_payment_product_id and l.qty > 0 and l.sale_order_origin_id):
    #             sale_lines = line.sale_order_origin_id.order_line
    #             sale_line = self.env['sale.order.line'].create({
    #                 'order_id': line.sale_order_origin_id.id,
    #                 'product_id': line.product_id.id,
    #                 'price_unit': line.price_unit,
    #                 'product_uom_qty': 0,
    #                 'tax_id': [(6, 0, line.tax_ids.ids)],
    #                 'is_downpayment': True,
    #                 'discount': line.discount,
    #                 'sequence': sale_lines and sale_lines[-1].sequence + 1 or 10,
    #             })
    #             sale_line._compute_tax_id()
    #             line.sale_order_line_id = sale_line
    #
    #         so_lines = order.lines.mapped('sale_order_line_id')
    #
    #         # confirm the unconfirmed sale orders that are linked to the sale order lines
    #         sale_orders = so_lines.mapped('order_id')
    #         for sale_order in sale_orders.filtered(lambda so: so.state in ['draft', 'sent']):
    #             sale_order.action_confirm()
    #
    #         # update the demand qty in the stock moves related to the sale order line
    #         # flush the qty_delivered to make sure the updated qty_delivered is used when
    #         # updating the demand value
    #         so_lines.flush(['qty_delivered'])
    #         # track the waiting pickings
    #         waiting_picking_ids = set()
    #         for so_line in so_lines:
    #             for stock_move in so_line.move_ids:
    #                 picking = stock_move.picking_id
    #                 if not picking.state in ['waiting', 'confirmed', 'assigned']:
    #                     continue
    #                 new_qty = so_line.product_uom_qty - so_line.qty_delivered
    #                 if float_compare(new_qty, 0, precision_rounding=stock_move.product_uom.rounding) <= 0:
    #                     new_qty = 0
    #                 stock_move.product_uom_qty = so_line.product_uom._compute_quantity(new_qty, stock_move.product_uom,
    #                                                                                    False)
    #                 waiting_picking_ids.add(picking.id)
    #
    #         def is_product_uom_qty_zero(move):
    #             return float_is_zero(move.product_uom_qty, precision_rounding=move.product_uom.rounding)
    #
    #         # cancel the waiting pickings if each product_uom_qty of move is zero
    #         for picking in self.env['stock.picking'].browse(waiting_picking_ids):
    #             if all(is_product_uom_qty_zero(move) for move in picking.move_lines):
    #                 picking.action_cancel()
    #
    #             picking.write({'state_paye': True})
    #
    #     self.env['stock.picking'].browse(waiting_picking_ids).write({'state_paye': True})
    #     return order_ids
