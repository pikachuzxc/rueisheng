# -*- coding:utf-8 -*-
from odoo import models,api,fields

class GeneImpactMedicine(models.Model):
    _name = 'gene.impact.medicine'

    impact_code = fields.Many2one(comodel_name='gene.impact', string='檢體資料')
    medicine_code = fields.Many2one(comodel_name='medicine.data', string='藥物')


