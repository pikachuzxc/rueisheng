# -*- coding:utf-8 -*-
from odoo import models,api,fields

class RuGene(models.Model):
    _name = 'ru.gene'

    gene = fields.Char('基因')
    gene_medicine = fields.Many2many(comodel_name='ru.medicine', string='基因')


    # def import_gene_impact(self):
    #     action = self.env.ref('gene_base.gene_impact_action').read()[0]
    #     action['context'] = {'default_subject_code': self.id}
    #     action['domain'] = [('subject_code', '=', self.id)]
    #     return action

    @api.multi
    def name_get(self):
        result = []
        for record in self:
            name = "%s" % (record.gene)
            result.append((record.id, name))
        return result


