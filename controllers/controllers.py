

from odoo import http
from odoo import SUPERUSER_ID
from odoo.exceptions import AccessError, MissingError, ValidationError


class BtDuong(http.Controller):
    @http.route('/create_lead', type='json', auth='none')
    def create_lead(self):
        """
        Demo api call:
        {
            "name":"name 1",
            "type": "opportunity",
            "partner_id": 3,
            "date_deadline": "2024-07-01",
            "email_cc": "test@example.com",
            "phone": "123456789",
            "description": "Test lead creation",
            "custom_requests": [
                {
                "product_id": 1,
                "date": "2024-07-01",
                "description": "Request description 1",
                "qty": 10
                },
                {
                "product_id": 1,
                "date": "2024-07-02",
                "description": "Request description 2",
                "qty": 5
                }
            ]
        }
        """
        try:
            vals = http.request.get_json_data()
            lead = http.request.env['crm.lead'].with_user(SUPERUSER_ID).sudo().create({
                'name': vals.get('name'),
                'type': vals.get('type'),
                'partner_id': vals.get('partner_id'),
                'date_deadline': vals.get('date_deadline'),
                'email_cc': vals.get('email_cc'),
                'phone': vals.get('phone'),
                'description': vals.get('description'),
            })

            if 'custom_requests' in vals and isinstance(vals.get('custom_requests'), list):
                custom_requests = vals.get('custom_requests')
                for value in custom_requests:
                    product_id = value.get('product_id')
                    date = value.get('date')
                    description = value.get('description')
                    qty = value.get('qty')
                    custom_request = http.request.env['crm.customer.request'].with_user(SUPERUSER_ID).sudo().create({
                        'opportunity_id': lead.id,
                        'product_id': product_id,
                        'date': date,
                        'description': description,
                        'qty': qty,
                    })
            return {
                'message':'Add record successfully',
                'id': lead.id
            }
        except(AccessError, MissingError):
            return

