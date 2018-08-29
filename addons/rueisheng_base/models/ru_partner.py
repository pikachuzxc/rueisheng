# -*- coding:utf-8 -*-

from odoo import api,fields,models

class RuPartner(models.Model):

    _name = "ru.partner"

    # 報告標題
    # title_chi = fields.Many2one(comodel_name='title.id', string='報告中文標題')
    # title_eng = fields.Char('報告英文標題', compute='set_title_eng')
    report_date = fields.Date('報告日期')

    # 受測者基本資料
    name = fields.Char(string='姓名', required = True)
    sex = fields.Selection([(1,'男'),(2,'女')],string='性別')
    birth = fields.Date('出生日期')
    phone = fields.Char('連絡電話')
    id_card = fields.Char('身分證字號')
    address = fields.Char('通訊地址')
    email = fields.Char('電子信箱')
    client_code = fields.Char('委託單位')



# 呼叫報表
    def call_print_report(self):
        datas = {
            'male': self.male,
            'female': self.female
        }
        return self.env['report'].get_action([], 'rueisheng_base.ru_partner', datas)

from odoo.addons.report_doc.report.report_doc import GeneReportWord
class GeneReportDocx(GeneReportWord):

    def generate_word_report(self, document, data, objs, report):
    #
    #     gene_data = list()
    #     gene_impact = list()
    #     medicine_data = list()
    #     gene_data_fir = list()
        male = ""
        female = ""
    #     TSOne = ""
    #     TSCancer = ""
    #     TSColon = ""
    #     BRCAL = ""
    #     TSLung = ""
    #     TSBreast = ""
    #     Other_test = ""
    #     test = u'I love \u001b[0;32m Stack Overflow \u001b[0m'
    #
        for line in objs:

                if line.sex == 1:
                    male = u"■"
                    female = u"□"
                else:
                    male = u"□"
                    female = u"■"
    #
    #             if line.TSOne == True:
    #                 TSOne = u"■"
    #             else:
    #                 TSOne = u"□"
    #
    #             if line.TSCancer == True:
    #                 TSCancer = u"■"
    #             else:
    #                 TSCancer = u"□"
    #
    #             if line.TSColon == True:
    #                 TSColon = u"■"
    #             else:
    #                 TSColon = u"□"
    #
    #             if line.BRCAL == True:
    #                 BRCAL = u"■"
    #             else:
    #                 BRCAL = u"□"
    #
    #             if line.TSLung == True:
    #                 TSLung = u"■"
    #             else:
    #                 TSLung = u"□"
    #
    #
    #             if line.TSBreast == True:
    #                 TSBreast = u"■"
    #             else:
    #                 TSBreast = u"□"
    #
    #
    #             if line.Other_test == True:
    #                 Other_test = u"■"
    #             else:
    #                 Other_test = u"□"
    #
    #
    #
    #
    #             for data in line.sequence_variation_code:
    #                 A = ""
    #                 B = ""
    #                 C = ""
    #                 D = ""
    #
    #                 if data.A == True:
    #                     A = u"•"
    #                 else:
    #                     A = ""
    #
    #                 if data.B == True:
    #                     B = u"•"
    #                 else:
    #                     B = ""
    #
    #                 if data.C == True:
    #                     C = u"•"
    #                 else:
    #                     C = ""
    #
    #                 if data.D == True:
    #                     D = u"•"
    #                 else:
    #                     D = ""
    #
    #                 gene_data.append({'chromosome' : str(data.chromosome)  ,'gene': data.gene,
    #                                   'total_sequence_variation' : str(data.total_sequence_variation),
    #                                   'SNV' : str(data.SNV),'INDEL' : str(data.INDEL),
    #                                   'M_SE' : str(data.M_SE),'N_SE' : str(data.N_SE),
    #                                   'SYN' : str(data.SYN),'UTR1' : str(data.UTR1),
    #                                   'UTR2' : str(data.UTR2), 'INGE' : str(data.INGE),
    #                                   'INTR': str(data.INTR),
    #                                   'A' : A, 'B' : B,
    #                                   'C': C, 'D' : D})
    #             for data in line.gene_impact_code:
    #                 gene_impact.append({'category':data.category,'gene': data.gene,'type': data.type,
    #                                     'codingConsequence':data.codingConsequence,'var_percent':data.var_percent,
    #                                     'c_DNA':data.c_DNA,'protein':data.new_protein})
    #
    #             for row in line.gene_impact_code[0].impact_medicine_code:
    #
    #                 medicine_data.append({'medic_name':row[0].medicine_code.medic_name,'pharmacist':row[0].medicine_code.pharmacist,
    #                                       'development_phase': row[0].medicine_code.development_phase, 'USFDA': row[0].medicine_code.USFDA,
    #                                       'TFDA': row[0].medicine_code.TFDA, 'health_insurance_provided': row[0].medicine_code.health_insurance_provided})


                document.merge(
                    # title_chi=line.title_chi.name,
                    # title_eng=line.title_eng,
                    report_date=str(line.report_date),
                    name = line.name,
                    male = male,
                    female = female,
                    birth = str(line.birth),
                    phone = line.phone,
                    id_card = line.id_card,
                    address = line.address,
                    email = line.email,
                    client_code = line.client_code,

                    # disease_text = line.disease_text,
                    # TSOne = TSOne,
                    # TSCancer = TSCancer,
                    # TSColon = TSColon,
                    # BRCAL = BRCAL,
                    # TSLung = TSLung,
                    # TSBreast = TSBreast,
                    # Other_test = Other_test,
                    # test_result = line.test_result,
                    # submission_date = line.submission_date,
                    # receipt_date = line.receipt_date,
                    # check_number=line.check_number,
                    # execute_date = line.execute_date,
                    # patient_number=line.patient_number,
                    # sample_number=line.sample_number,
                    # lab_manager=line.lab_manager,
                    # report_sign=line.report_sign,
                    # sample_id = line.sample_id,
                    # pathology=line.pathology,
                    # sample_resource_code=line.sample_resource_code.name,
                    # DNA_extract_code=line.DNA_extract_code.name,
                    # sequence_set=line.sequence_set,
                    # sequence_platform_code=line.sequence_platform_code.name,
                    # sequence_mode=line.sequence_mode,
                    # Prelim_lib=str(line.Prelim_lib),
                    # Comparison_data=line.Comparison_data,
                    # human_reading=str(line.human_reading),
                    # human_percent=str(line.human_percent),
                    # target_reading=str(line.target_reading),
                    # target_percent=str(line.target_percent),
                    # sequence_cover=str(line.sequence_cover),
                    # lab_address=line.lab_address,
                    # gene_fir=line.gene_impact_code[0].gene,
                    # codingConsequence_fir=line.gene_impact_code[0].codingConsequence,
                    # var_percent_fir=line.gene_impact_code[0].var_percent,
                    # protein_fir=line.gene_impact_code[0].new_protein,
                    # sequence_depth_fir=line.gene_impact_code[0].sequence_depth,

                )
                # document.merge_rows('chromosome', gene_data)
                # document.merge_rows('gene', gene_impact)
                # document.merge_rows('medic_name', medicine_data)



GeneReportDocx('report.rueisheng_base.cancer_report', 'ru.partner')