# -*- coding:utf-8 -*-
import os
import requests
from odoo import models,api,fields

class ReportDoc(models.Model):
    _name = 'report.doc'

    name = fields.Char('文件名稱')
    document = fields.Binary('文件')
    path = fields.Char('路徑')

    @api.onchange('document')
    def inverse_datas(self):
        if self.document != False:
            dirname = os.path.dirname('../addons/report_doc/')
            data = self.document.decode('base64')
            path = dirname + '/' + self.name + u".docx"
            with open(path, 'wb') as w:
                w.write(data)
            self.update({
                'path': path
            })
# dirname = os.path.dirname('/odoo/custom/addons/report_doc/')
# dirname = os.path.dirname('../addons/report_doc/')
# update / write
# dirname 在gcp要用絕對路徑不能用相對路徑