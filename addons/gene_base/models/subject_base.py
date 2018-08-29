# -*- coding:utf-8 -*-

from odoo import api,fields,models

class SubjectBase(models.Model):

    _name = "subject.base"

    # 報告標題
    title_chi = fields.Many2one(comodel_name='title.id',string='報告中文標題')
    title_eng = fields.Char('報告英文標題',compute='set_title_eng')
    report_date = fields.Date('報告日期')

    # 受測者基本資料

    name = fields.Many2one(comodel_name='patient.data',string='姓名')
    sex = fields.Selection([(1,'男'),(2,'女')],string='性別',readonly=True)
    birth = fields.Date('出生日期',readonly=True)
    phone = fields.Char('連絡電話',readonly=True)
    id_card = fields.Char('身分證字號',readonly=True,compute='set_petient_data')
    address = fields.Char('通訊地址',readonly=True)
    email = fields.Char('電子信箱',readonly=True)
    client_code = fields.Many2one(comodel_name='client.company',string='委託單位')

    # 檢測項目

    TSOne = fields.Boolean('TSOne')
    TSCancer = fields.Boolean('TSCancer')
    TSColon = fields.Boolean('TSColon')
    BRCAL = fields.Boolean('BRCAL1/BRCAL2')
    TSLung = fields.Boolean('TSLung')
    TSBreast = fields.Boolean('TSBreast')
    Other_test = fields.Boolean('Other test')


    disease_text = fields.Text('病例簡述')



    # 檢測結果
    test_result = fields.Text('檢測結果')
    submission_date = fields.Date('送檢日期')
    receipt_date = fields.Date('收件日期')
    check_number = fields.Char('送驗單編號') #many2one
    execute_date = fields.Date('執行時間')
    patient_number = fields.Char('病歷編號') #many2one
    sample_number = fields.Char('樣品編號') #many2one
    lab_manager = fields.Char('實驗室主管') #many2one
    report_sign = fields.Char('報告簽署人') #many2one

    #定序實驗結果說明
    sample_id = fields.Char('樣本編號') #many2one
    pathology = fields.Char('病理特性')
    sample_resource_code = fields.Many2one(comodel_name='sample.resource',string='檢體來源')
    DNA_extract_code = fields.Many2one(comodel_name='dna.extract',string='DNA萃取方式')
    sequence_set = fields.Char('定序集庫製備')
    sequence_platform_code = fields.Many2one(comodel_name='sequence.platform',string='定序平台')
    sequence_mode = fields.Char('定序模式')
    Prelim_lib = fields.Integer('初步集庫讀數')
    Comparison_data = fields.Char('比對資料庫')
    human_reading = fields.Integer('比對至人類序列讀數')
    human_percent = fields.Float('比對至人類序列比例')
    target_reading = fields.Integer('比對至目標序列讀數')
    target_percent = fields.Float('比對至目標序列比例')
    sequence_cover = fields.Integer('10%分位序列覆蓋率')
    lab_address = fields.Char('實驗室地址')

    # 關聯
    sequence_variation_code = fields.One2many(comodel_name='sequence.variation.table', inverse_name='subject_code', string='序列變異')
    gene_impact_code = fields.One2many(comodel_name='gene.impact', inverse_name='subject_code', string='基因功能影響')

    @api.depends('title_chi')
    def set_title_eng(self):
            self.title_eng = self.title_chi.name_eng
            self.TSOne = self.title_chi.TSOne
            self.TSCancer = self.title_chi.TSCancer
            self.TSColon = self.title_chi.TSColon
            self.BRCAL = self.title_chi.BRCAL
            self.TSLung = self.title_chi.TSLung
            self.TSBreast = self.title_chi.TSBreast
            self.Other_test = self.title_chi.Other_test

    @api.depends('name')
    def set_petient_data(self):
            self.sex = self.name.sex
            self.birth = self.name.birth
            self.phone = self.name.phone
            self.id_card = self.name.id_card
            self.address = self.name.address
            self.email = self.name.email

    def import_gene_impact(self):
        action = self.env.ref('gene_base.gene_impact_action').read()[0]
        action['context'] = {'default_subject_code': self.id}
        action['domain'] = [('subject_code', '=', self.id)]
        return action

    def import_sequence_variation(self):
        action = self.env.ref('gene_base.sequence_variation_table_action').read()[0]
        action['context'] = {'default_subject_code': self.id}
        action['domain'] = [('subject_code', '=', self.id)]
        return action

    def delete_off_target_data(self):
        self.env['gene.impact'].search([('subject_code','=',self.id),('filter','like','off_target%')]).unlink()

    def delete_c_dna_field_c_point(self):
        for line in self.gene_impact_code:
            line.c_DNA = str(line.c_DNA).strip('c.')
            if line.protein is False:
                continue
            else:
                line.new_protein = str(line.protein).strip('p.=')
                line.new_protein = str(line.new_protein).strip(" (p. % )")

from odoo.addons.report_doc.report.report_doc import GeneReportWord
class GeneReportDocx(GeneReportWord):

    def generate_word_report(self, document, data, objs, report):

        gene_data = list()
        gene_impact = list()
        medicine_data = list()
        gene_data_fir = list()
        male = ""
        female = ""
        TSOne = ""
        TSCancer = ""
        TSColon = ""
        BRCAL = ""
        TSLung = ""
        TSBreast = ""
        Other_test = ""
        test = u'I love \u001b[0;32m Stack Overflow \u001b[0m'

        for line in objs:

                if line.sex == 1:
                    male = u"■"
                    female = u"□"
                else:
                    male = u"□"
                    female = u"■"

                if line.TSOne == True:
                    TSOne = u"■"
                else:
                    TSOne = u"□"

                if line.TSCancer == True:
                    TSCancer = u"■"
                else:
                    TSCancer = u"□"

                if line.TSColon == True:
                    TSColon = u"■"
                else:
                    TSColon = u"□"

                if line.BRCAL == True:
                    BRCAL = u"■"
                else:
                    BRCAL = u"□"

                if line.TSLung == True:
                    TSLung = u"■"
                else:
                    TSLung = u"□"


                if line.TSBreast == True:
                    TSBreast = u"■"
                else:
                    TSBreast = u"□"


                if line.Other_test == True:
                    Other_test = u"■"
                else:
                    Other_test = u"□"




                for data in line.sequence_variation_code:
                    A = ""
                    B = ""
                    C = ""
                    D = ""

                    if data.A == True:
                        A = u"•"
                    else:
                        A = ""

                    if data.B == True:
                        B = u"•"
                    else:
                        B = ""

                    if data.C == True:
                        C = u"•"
                    else:
                        C = ""

                    if data.D == True:
                        D = u"•"
                    else:
                        D = ""

                    gene_data.append({'chromosome' : str(data.chromosome)  ,'gene': data.gene,
                                      'total_sequence_variation' : str(data.total_sequence_variation),
                                      'SNV' : str(data.SNV),'INDEL' : str(data.INDEL),
                                      'M_SE' : str(data.M_SE),'N_SE' : str(data.N_SE),
                                      'SYN' : str(data.SYN),'UTR1' : str(data.UTR1),
                                      'UTR2' : str(data.UTR2), 'INGE' : str(data.INGE),
                                      'INTR': str(data.INTR),
                                      'A' : A, 'B' : B,
                                      'C': C, 'D' : D})
                for data in line.gene_impact_code:
                    gene_impact.append({'category':data.category,'gene': data.gene,'type': data.type,
                                        'codingConsequence':data.codingConsequence,'var_percent':data.var_percent,
                                        'c_DNA':data.c_DNA,'protein':data.new_protein})

                for row in line.gene_impact_code[0].impact_medicine_code:

                    medicine_data.append({'medic_name':row[0].medicine_code.medic_name,'pharmacist':row[0].medicine_code.pharmacist,
                                          'development_phase': row[0].medicine_code.development_phase, 'USFDA': row[0].medicine_code.USFDA,
                                          'TFDA': row[0].medicine_code.TFDA, 'health_insurance_provided': row[0].medicine_code.health_insurance_provided})







                document.merge(
                    name = line.name,
                    male = male,
                    female = female,
                    title_chi = line.title_chi.name,
                    title_eng = line.title_eng,
                    report_date = str(line.report_date),
                    birth = str(line.birth),
                    phone = line.phone,
                    id_card = line.id_card,
                    address = line.address,
                    email = line.email,
                    entrustment_company = line.entrustment_company,
                    disease_text = line.disease_text,
                    TSOne = TSOne,
                    TSCancer = TSCancer,
                    TSColon = TSColon,
                    BRCAL = BRCAL,
                    TSLung = TSLung,
                    TSBreast = TSBreast,
                    Other_test = Other_test,
                    test_result = line.test_result,
                    submission_date = line.submission_date,
                    receipt_date = line.receipt_date,
                    execute_date = line.execute_date,
                    check_number=line.check_number,
                    patient_number=line.patient_number,
                    sample_number=line.sample_number,
                    lab_manager=line.lab_manager,
                    report_sign=line.report_sign,
                    sample_id = line.sample_id,
                    pathology=line.pathology,
                    sample_resource_code=line.sample_resource_code.name,
                    DNA_extract_code=line.DNA_extract_code.name,
                    sequence_set=line.sequence_set,
                    sequence_platform_code=line.sequence_platform_code.name,
                    sequence_mode=line.sequence_mode,
                    Prelim_lib=str(line.Prelim_lib),
                    Comparison_data=line.Comparison_data,
                    human_reading=str(line.human_reading),
                    human_percent=str(line.human_percent),
                    target_reading=str(line.target_reading),
                    target_percent=str(line.target_percent),
                    sequence_cover=str(line.sequence_cover),
                    lab_address=line.lab_address,
                    gene_fir=line.gene_impact_code[0].gene,
                    codingConsequence_fir=line.gene_impact_code[0].codingConsequence,
                    var_percent_fir=line.gene_impact_code[0].var_percent,
                    protein_fir=line.gene_impact_code[0].new_protein,
                    sequence_depth_fir=line.gene_impact_code[0].sequence_depth,

                )
                document.merge_rows('chromosome', gene_data)
                document.merge_rows('gene', gene_impact)
                document.merge_rows('medic_name', medicine_data)



GeneReportDocx('report.gene_base.cancer_report', 'subject.base')