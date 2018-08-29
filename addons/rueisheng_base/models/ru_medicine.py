# -*- coding:utf-8 -*-

from odoo import models,api,fields

class RuMedicine(models.Model):
    _name = 'ru.medicine'

    medicine_gene = fields.Many2many(comodel_name='ru.gene',string='藥物')


    medic_name = fields.Char('藥名')
    trade_name = fields.Char('商標名')
    type = fields.Char('種類')
    FDA = fields.Char('FDA approved 適應症 ')
    pharmacist = fields.Char('藥商')
    TFDA = fields.Selection([(1, '有'), (2, '無')], string='TFDA 通過')
    health_insurance_provided = fields.Selection(selection=[(1, '給付'), (2, '無給付'), (3, '─')], string='健保給付')


    @api.multi
    def name_get(self):
        result = []
        for record in self:
            name = "%s" % (record.medic_name)
            result.append((record.id, name))
        return result