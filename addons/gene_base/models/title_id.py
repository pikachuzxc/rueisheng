# -*- coding:utf-8 -*-

from odoo import api,fields,models

class SubjectBase(models.Model):

    _name = "title.id"

    name = fields.Char('癌症中文名稱')
    name_eng = fields.Char('癌症英文名稱')
    TSOne = fields.Boolean('TSOne')
    TSCancer = fields.Boolean('TSCancer')
    TSColon = fields.Boolean('TSColon')
    BRCAL = fields.Boolean('BRCAL1/BRCAL2')
    TSLung = fields.Boolean('TSLung')
    TSBreast = fields.Boolean('TSBreast')
    Other_test = fields.Boolean('Other test')
    sequence_variation_code = fields.One2many(comodel_name='sequence.variation.table', inverse_name='subject_code',
                                              string='序列變異')

class DnaExtract(models.Model):

    _name = "dna.extract"
    name = fields.Char('DNA萃取方式')


class SampleResource(models.Model):

    _name = "sample.resource"
    name = fields.Char('檢體來源')

class SequencePlatform(models.Model):

    _name = "sequence.platform"
    name = fields.Char('定序平台')

class ClientCompany(models.Model):
    _name = "client.company"
    name = fields.Char('委託單位')
