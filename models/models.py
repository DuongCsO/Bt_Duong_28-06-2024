# -*- coding: utf-8 -*-

# from odoo import models, fields, api


# class bt_duong(models.Model):
#     _name = 'bt_duong.bt_duong'
#     _description = 'bt_duong.bt_duong'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100
