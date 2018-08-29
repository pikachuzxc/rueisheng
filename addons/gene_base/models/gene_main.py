# -*- coding: utf-8 -*-

from odoo import models, fields, api

class GeneMain(models.Model):
    _name = 'gene.main'

    name = fields.Char(string='主檔名稱')
    person_id = fields.Many2one(comodel_name='res.users', string='基因所有人')
    gene_ids = fields.One2many(comodel_name='gene.base', inverse_name='parent_id')
    test_field = fields.Char(string='測試用字串')

    def import_gene_excel(self):
        action = self.env.ref('gene_base.gene_base_view_action').read()[0]
        action['context'] = {'default_parent_id': self.id}
        action['domain'] = [('parent_id', '=', self.id)]
        return action

from odoo.addons.report_doc.report.report_doc import GeneReportWord

class GeneReportDocx(GeneReportWord):

    def generate_word_report(self, document, data, objs, report):
        for line in objs:
            document.merge(
                name=line.name,
                gene_ids=line.person_id.name,
                test_field=line.test_field,
            )




GeneReportDocx('report.gene_base.gene_report', 'gene.main')