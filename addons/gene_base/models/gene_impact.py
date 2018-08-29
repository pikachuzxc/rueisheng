# -*- coding:utf-8 -*-
from odoo import models,api,fields

class GeneImpact(models.Model):
    _name = 'gene.impact'


    category = fields.Char('影響程度')
    gene = fields.Char('基因')
    type = fields.Char('序列變異')
    codingConsequence = fields.Char('基因變異')
    var_percent = fields.Char('變異比例')
    c_DNA = fields.Char('序列變異說明')
    new_protein = fields.Char('蛋白質變異說明')
    sequence_depth = fields.Char('定序深度')
    filter = fields.Char('')

    subject_code = fields.Many2one(comodel_name='subject.base', string='檢體資料')
    impact_medicine_code = fields.One2many(comodel_name='gene.impact.medicine', inverse_name='impact_code', string='藥物資料')

    # 資料匯入的原始檔
    c_DNA = fields.Char('序列變異說明')
    protein = fields.Char('蛋白質變異說明')