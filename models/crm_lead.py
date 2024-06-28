from odoo import models, fields, api

class CrmLead(models.Model):
    _inherit = 'crm.lead'

    request_ids = fields.One2many('crm.customer.request', 'opportunity_id', string='Customer Request')

    total_qty = fields.Float(compute='_compute_total_qty', string='Total Quantity')

    expected_revenue = fields.Monetary(
        'Expected Revenue',
        currency_field='company_currency',
        tracking=True,
        compute='_compute_revenue',
    )

    @api.depends('request_ids.qty')
    def _compute_total_qty(self):
        for lead in self:
            lead.total_qty = sum(request.qty for request in lead.request_ids)

    @api.depends('request_ids.qty','request_ids.product_id.standard_price','request_ids.product_id.list_price')
    def _compute_revenue(self):
        for lead in self:
            lead.expected_revenue = sum(request.qty*(request.product_id.standard_price-request.product_id.list_price) for request in lead.request_ids)
