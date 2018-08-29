# -*- coding:utf-8 -*-
from odoo import models,api,fields

class RuDetect(models.Model):
    _name = 'ru.detect'

    detect = fields.Char('檢測項目')


    # def import_gene_impact(self):
    #     action = self.env.ref('gene_base.gene_impact_action').read()[0]
    #     action['context'] = {'default_subject_code': self.id}
    #     action['domain'] = [('subject_code', '=', self.id)]
    #     return action

    # @api.multi
    # def name_get(self):
    #     result = []
    #     for record in self:
    #         name = "%s" % (record.gene)
    #         result.append((record.id, name))
    #     return result


