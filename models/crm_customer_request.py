from odoo import models, fields, api, SUPERUSER_ID

class CrmCustomerRequest(models.Model):
    _name = 'crm.customer.request'
    _description = 'Customer Request'

    product_id = fields.Many2one('product.template', string='Product', required=True)
    opportunity_id = fields.Many2one('crm.lead', string='Opportunity', required=True)
    date = fields.Date(string='Date', required=True, default=fields.Date.today)
    description = fields.Text(string='Description')
    qty = fields.Float(string='Quantity', default=1)
