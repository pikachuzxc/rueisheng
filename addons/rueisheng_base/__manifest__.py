# -*- coding: utf-8 -*-
{
    'name': "rueisheng_base",
    'version': '1.0',
    'depends': [],
    'author': "先傑電腦",
    'website': "http://www.alltop.com/",
    'category': '',
    'description': """
    """,
    'depends': [
        'base',
        'report_doc'
    ],
    'data': [
        # 'security/ir.model.access.csv',
        'views/ru_medical.xml',
        'views/report_doc.xml',
        'views/ru_detect.xml',
        'views/ru_gene.xml',
        'views/ru_medicine.xml',
        'views/ru_partner.xml',
        'views/charity_view.xml',
    ],
    # only loaded in demonstration mode

}