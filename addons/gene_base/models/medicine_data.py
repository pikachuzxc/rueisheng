# -*- coding:utf-8 -*-

from odoo import models,api,fields

class MedicineImpact(models.Model):
    _name = 'medicine.data'


    medic_name = fields.Char('藥物名')
    pharmacist = fields.Char('藥商')
    development_phase = fields.Char('研發階段')
    USFDA = fields.Char('USFDA')
    TFDA = fields.Char('TFDA')
    health_insurance_provided = fields.Char('健保給付')

    impact_code = fields.Many2one(comodel_name='gene.impact', string='檢體資料')

    @api.multi
    def name_get(self):
        result = []
        for record in self:
            name = "%s" % (record.medic_name)
            result.append((record.id, name))
        return result