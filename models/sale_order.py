from odoo import models, fields, api

class SaleOrder(models.Model):
    _inherit='sale.order'


    order_line = fields.One2many(
        comodel_name='sale.order.line',
        inverse_name='order_id',
        string="Order Lines",
        copy=True, auto_join=True, compute='set_product_request')

    @api.depends('opportunity_id','order_line')
    def set_product_request(self):
        for record in self:
            order_lines = self.env['sale.order.line']
            for request in record.opportunity_id.request_ids:
                order_line = self.env['sale.order.line'].create({
                    'order_id': record.id,
                    'product_id': request.product_id.id,
                    'product_uom_qty': request.qty,
                })
                order_lines += order_line
            record.order_line=order_lines
