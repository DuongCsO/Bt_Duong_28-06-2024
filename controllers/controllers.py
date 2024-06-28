
from odoo import http


class BtDuong(http.Controller):
    @http.route('/create_lead', methods=['POST'], type='json', auth='none')
    def create_lead(self, **kwargs):
        lead = http.request.env['crm.lead'].sudo().create({
            'name': kwargs.get('name'),
            'type': kwargs.get('type'),
            'partner_id': kwargs.get('partner_id'),
            'date_deadline': kwargs.get('date_deadline'),
            'email_cc': kwargs.get('email_cc'),
            'phone': kwargs.get('phone'),
            'description': kwargs.get('description'),
        })
        custom_requests_data = kwargs.get('custom_requests', [])
        custom_requests = []
        
        for req_data in custom_requests_data:
            product_id = req_data.get('product_id')
            date = req_data.get('date')
            description = req_data.get('description')
            qty = req_data.get('qty')
            custom_request = http.request.env['crm.customer.request'].sudo().create({
                'product_id': product_id,
                'date': date,
                'description': description,
                'qty': qty,
            })

#     @http.route('/bt_duong/bt_duong', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/bt_duong/bt_duong/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('bt_duong.listing', {
#             'root': '/bt_duong/bt_duong',
#             'objects': http.request.env['bt_duong.bt_duong'].search([]),
#         })

#     @http.route('/bt_duong/bt_duong/objects/<model("bt_duong.bt_duong"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('bt_duong.object', {
#             'object': obj
#         })
