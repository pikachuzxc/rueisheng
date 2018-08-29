# -*- coding:utf-8 -*-

from odoo import api,fields,models

class PatientData(models.Model):

    _name = "patient.data"

    name = fields.Char('姓名')
    sex = fields.Selection([(1, '男'), (2, '女')])
    birth = fields.Date('出生日期')
    phone = fields.Char('連絡電話')
    id_card = fields.Char('身分證字號')
    address = fields.Char('通訊地址')
    email = fields.Char('電子信箱')