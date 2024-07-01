from odoo import models, fields, api
from odoo import SUPERUSER_ID

class SaleOrder(models.Model):
    _inherit='sale.order'

    request_check = fields.Boolean(compute='set_product_request', store=True)

    @api.depends('create_date')
    def set_product_request(self):
        for record in self:
            # if record.id:
            list_request_id = self.env['crm.customer.request'].search([('opportunity_id','=',record.opportunity_id.id)])
            for customer_request in list_request_id:
                order_lines = self.env['sale.order.line'].search([('request_id','=', customer_request.id)])
                for o in order_lines:
                    o.unlink()
                if True:
                    order_line = self.env['sale.order.line'].with_user(SUPERUSER_ID).sudo().create({
                        'order_id': record.id,
                        'product_id': customer_request.product_id.id,
                        'product_uom_qty': customer_request.qty,
                        'request_id': customer_request.id,
                    })