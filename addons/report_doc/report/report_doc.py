# -*- coding: utf-8 -*-

import cStringIO
from odoo.report.report_sxw import report_sxw
from odoo.api import Environment
from mailmerge import MailMerge

template = u"../addons/report_doc/檢測報告.docx"


class GeneReportWord(report_sxw):

    def create(self, cr, uid, ids, data, context=None):
        self.env = Environment(cr, uid, context)
        report_obj = self.env['ir.actions.report.xml']
        report = report_obj.search([('report_name', '=', self.name[7:])])
        if report.ids:
            self.title = report.name
            if report.report_type == 'docx':
                return self.create_word_report(ids, data, report)
        return super(GeneReportWord, self).create(cr, uid, ids, data, context)

    def create_word_report(self, ids, data, report):
        path_data = self.env['report.doc'].search([('name','=',u'檢測報告')])
        template = path_data.path
        self.parser_instance = self.parser(
            self.env.cr, self.env.uid, self.name2, self.env.context)
        objs = self.getObjects(
            self.env.cr, self.env.uid, ids, self.env.context)
        self.parser_instance.set_context(objs, data, ids, 'docx')
        file_data = cStringIO.StringIO()
        document = MailMerge(template)
        self.generate_word_report(document, data, objs, report)
        document.write(file_data)
        document.close()
        file_data.seek(0)
        return (file_data.read(), 'docx')

    def generate_word_report(self, document, data, objs, report):
        raise NotImplementedError()
