# -*- coding:utf-8 -*-

from odoo import models,api,fields

class SequenceVariationTable(models.Model):
    _name = 'sequence.variation.table'

    chromosome = fields.Char('染色體')
    gene = fields.Char('基因')
    total_sequence_variation = fields.Integer('總序列變異數')
    SNV = fields.Integer(string='SNV')
    INDEL = fields.Integer(string='INDEL')
    M_SE = fields.Integer(string='M_SE')
    N_SE = fields.Integer(string='N_SE')
    SYN = fields.Integer(string='SYN')
    UTR1 = fields.Integer(string='3UTR')
    UTR2 = fields.Integer(string='5UTR')
    INGE = fields.Integer(string='INGE')
    INTR = fields.Integer(string='INTR')
    A = fields.Boolean('A')
    B = fields.Boolean('B')
    C = fields.Boolean('C')
    D = fields.Boolean('D')

    subject_code = fields.Many2one(comodel_name='subject.base',string='檢體資料')