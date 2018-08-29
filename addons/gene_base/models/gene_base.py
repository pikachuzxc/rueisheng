# -*- coding: utf-8 -*-
from odoo import models, fields, api


class GeneBase(models.Model):
    _name = 'gene.base'
    _description = u'匯入基因檔'

    parent_id = fields.Many2one(comodel_name='gene.main')
    name = fields.Char()
    category = fields.Char()
    gene = fields.Char()
    overlapKnown = fields.Char()
    type = fields.Char()
    codingConsequence = fields.Char()
    refGenome = fields.Char()
    chromosome = fields.Char()
    genome_position = fields.Char()
    depth = fields.Char()
    var_percent = fields.Char()
    exon_rank = fields.Char()
    cDNA = fields.Char()
    protein = fields.Char()
    ref = fields.Char()
    alt = fields.Char()
    refNum = fields.Char()
    altNum = fields.Char()
    refSeq = fields.Char()
    altSeq = fields.Char()
    refAA = fields.Char()
    altAA = fields.Char()
    tx_name = fields.Char()
    refSeqId = fields.Char()
    end = fields.Char()
    gene_boundaries = fields.Char()
    filter = fields.Char()
    hpflags = fields.Char()
    dbSNP = fields.Char()
    g1000 = fields.Char()
    esp5400 = fields.Char()
    cg69 = fields.Char()
    LJB_PhyloP = fields.Char()
    LJB_SIFT = fields.Char()
    LJB_PolyPhen2 = fields.Char()
    LJB_LRT = fields.Char()
    LJB_MutationTaster = fields.Char()
    LJB_GERP = fields.Char()
    id_cosmic_coding = fields.Char()
    info_cosmic_coding = fields.Char()
    id_cosmic_non_coding = fields.Char()
    info_cosmic_non_coding = fields.Char()
    gene_strand = fields.Char()
    ref1 = fields.Char()
    alt1 = fields.Char()
    first1 = fields.Char()
    last1 = fields.Char()
    extId = fields.Char()
    reason = fields.Char()
    in_report = fields.Char()
    seq = fields.Char()
    comment = fields.Char()
    reads = fields.Char()
    clinicsnp_type = fields.Char()
    pathogenicity_class = fields.Char()
    cDnaExtra = fields.Char()
    pos_in_exon = fields.Char()
    id_clinvar = fields.Char()
    exon_id = fields.Char()
    CN = fields.Char()
    label = fields.Char()
    status = fields.Char()
    screening_id = fields.Char()
    pred_cat = fields.Char()
    filterHistoric = fields.Char()
    reported = fields.Char()
    freq_batch = fields.Char()
    freq_client = fields.Char()
    freq_all = fields.Char()
    freq_all_total = fields.Char()
    experiment_type = fields.Char()
    P_COMMENT = fields.Char()
    PID = fields.Char()
    false_positived = fields.Char()
    falsePositive = fields.Char()
    F_COMMENT = fields.Char()
    PATHO_DISTRIB = fields.Char()
    flagged_region_id = fields.Char()
    ExAC = fields.Char()
    dist2exon = fields.Char()
    directScore = fields.Char()
    disease_clinicaltrial = fields.Char()
    sameDisease = fields.Char()
    geneActionable = fields.Char()
    partientDisease = fields.Char()
    clinicalTrialID = fields.Char()
    associationIDS = fields.Char()
    trID = fields.Char()
    associationID = fields.Char()
    CLNREVSTAT = fields.Char()
    CLNSIG = fields.Char()
    associationType = fields.Char()
    effectOnTreatment = fields.Char()
    PROCESSED_CLNSIG = fields.Char()
    CLNSIGLAB = fields.Char()
    LJB_PolyPhen2_HumDiv = fields.Char()
    OMIM = fields.Char()
    Other_type_pathogenicity = fields.Char()
    consistency_in_group = fields.Char()
























