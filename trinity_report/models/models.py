# -*- coding: utf-8 -*-

from odoo import models, fields, api, _
import datetime


class TrinityReport(models.Model):
    _name = 'trinity.report'
    _description = 'Trinity Report'
    _rec_name = 'e_examination_lrn'

    e_examination_nrn = fields.Char(string='E Examination NRN')
    e_examination_lrn = fields.Char(string='E Examination LRN', required=True, default=lambda self: _("New"))

    # Storing Patient Information. It is integrated with Trinity Patients module and will pull in all the patient's information.
    patient_identifier_id = fields.Many2one(comodel_name='patient.patient', string='Identifier', required=True)
    patient_title = fields.Selection(selection=[
            ('mr', 'Mr.'),
            ('mrs', 'Mrs.'),
            ('dr', 'Dr.'),
            ('prof', "Prof.")
        ], related='patient_identifier_id.title', store=True)
    patient_first_name = fields.Char(related='patient_identifier_id.first_name', store=True)
    patient_middle_name = fields.Char(related='patient_identifier_id.middle_name', store=True)
    patient_last_name = fields.Char(related='patient_identifier_id.last_name', store=True)
    patient_identifier_type = fields.Selection(selection=[
        ('personal_id', 'Personal ID'),
        ('personal_foreigner_id', 'Personal Foreigner ID'),
        ('social_security_no', 'Social Security Number'),
        ('passport_no', "Passport Number"),
        ('other_type', "Other Type"),
        ('newborn_id', "Newborn ID"),
    ], string='Identifier Type', related='patient_identifier_id.identifier_type', store=True)
    patient_birth_date = fields.Date(string='Birth Date', related='patient_identifier_id.birth_date', store=True)
    patient_health_region_id = fields.Many2one('health.region', string='Health Region', related='patient_identifier_id.health_region_id', store=True)
    patient_health_region_no = fields.Char(string='Health Region Number', related='patient_identifier_id.health_region_no', store=True)

    examination_open_dtm = fields.Datetime('Examination Open Date & Time', default=lambda self: datetime.datetime.now())
    # Will be 15 minutes ahead of examination open date & time
    examination_close_dtm = fields.Datetime('Examination Close Date & Time', default=lambda self: datetime.datetime.now() + datetime.timedelta(minutes=15))
    secondary_examination = fields.Selection(selection=[
        ('yes', 'Yes'),
        ('no', 'No')
    ], string='Is Secondary Examination', required=True, default='no')
    examination_purpose_id = fields.Many2one('examination.purpose', string='Examination Purpose')
    cost_bearer_id = fields.Many2one('trinity.insurance', string='Cost Bearer')

    # Storing Diagnosis Information
    icd_code = fields.Many2one(comodel_name='icd.diagnoses', string='ICD Code')
    additional_description = fields.Text(related='icd_code.diagnosis_bulgarian', store=True)
    icd_code1 = fields.Many2one(comodel_name='icd.diagnoses', string='ICD Code')
    additional_description1 = fields.Text(related='icd_code1.diagnosis_bulgarian', store=True)
    icd_code2 = fields.Many2one(comodel_name='icd.diagnoses', string='ICD Code')
    additional_description2 = fields.Text(related='icd_code2.diagnosis_bulgarian', store=True)
    icd_code3 = fields.Many2one(comodel_name='icd.diagnoses', string='ICD Code')
    additional_description3 = fields.Text(related='icd_code3.diagnosis_bulgarian', store=True)

    medical_history = fields.Text(string='Medical History')
    objective_condition = fields.Text(string='Objective Condition')
    assessment_notes = fields.Text(string='Assessment Notes')
    conclusion = fields.Text(string='Conclusion')

    # Doctor Performing Information; Integrated with Trinity Doctors Module
    dr_performing_doctor_id = fields.Many2one('trinity.doctor', string='ID of Medical Doctor', required=True)
    dr_performing_title = fields.Selection(selection=[
        ('mr', 'Mr.'),
        ('mrs', 'Mrs.'),
        ('dr', 'Dr.'),
        ('prof', "Prof.")
    ], related='dr_performing_doctor_id.title', store=True)
    dr_performing_first_name = fields.Char(string='Name', related='dr_performing_doctor_id.first_name', store=True)
    dr_performing_middle_name = fields.Char(related='dr_performing_doctor_id.middle_name', store=True)
    dr_performing_last_name = fields.Char(related='dr_performing_doctor_id.last_name', store=True)
    dr_performing_qualification_code_id = fields.Many2one('qualification.code', string='NHIF Code', related='dr_performing_doctor_id.qualification_code_id', store=True)
    dr_performing_speciality_id = fields.Many2one('doctor.speciality', string='NHIF Name', related='dr_performing_doctor_id.speciality_id', store=True)
    dr_performing_hospital_no = fields.Char(string='Hospital Number', related='dr_performing_doctor_id.hospital_no', store=True)

    # Doctor Directing Patient Information
    dr_directing_doctor_id = fields.Many2one('trinity.doctor.external', string='ID of Medical Doctor', required=True)
    dr_directing_title = fields.Selection(selection=[
        ('mr', 'Mr.'),
        ('mrs', 'Mrs.'),
        ('dr', 'Dr.'),
        ('prof', "Prof.")
    ], related='dr_directing_doctor_id.title', store=True)
    dr_directing_first_name = fields.Char(string='Name', related='dr_directing_doctor_id.first_name', store=True)
    dr_directing_middle_name = fields.Char(related='dr_directing_doctor_id.middle_name', store=True)
    dr_directing_last_name = fields.Char(related='dr_directing_doctor_id.last_name', store=True)
    dr_directing_qualification_code_id = fields.Many2one('qualification.code', string='NHIF Code',
                                                         related='dr_directing_doctor_id.qualification_code_id',
                                                         store=True)
    dr_directing_speciality_id = fields.Many2one('doctor.speciality', string='Speciality',
                                                 related='dr_directing_doctor_id.speciality_id', store=True)
    dr_directing_hospital_no = fields.Char(string='Hospital Number', related='dr_directing_doctor_id.hospital_no',
                                           store=True)

    originating_document_no = fields.Char(string='Original Document Number')
    date_originating_doc = fields.Date(string='Date of Originating Document')

    examination_type_id = fields.Many2one('examination.type', string='Type of Examination')
    examination_cost_id = fields.Many2one('examination.cost', string='Cost of Examination')

    @api.model
    def create(self, vals):
        if vals.get('e_examination_lrn', _('New')) == _('New'):
            vals['e_examination_lrn'] = self.env['ir.sequence'].next_by_code('lrn.number') or _('New')
        res = super(TrinityReport, self).create(vals)
        return res

    def reset_sequence_codes(self):
        seq_lrn = self.env['ir.sequence'].search([('code', '=', 'lrn.number')])
        seq_lrn.number_next_actual = 1


class ExaminationPurpose(models.Model):
    _name = 'examination.purpose'
    _description = 'Examination Purpose'

    name = fields.Char(required=True)


class ExaminationType(models.Model):
    _name = 'examination.type'
    _description = 'Examination Type'

    name = fields.Char(required=True)


class ExaminationCost(models.Model):
    _name = 'examination.cost'
    _description = 'Examination Cost'
    _rec_name = 'cost'

    cost = fields.Float(required=True)
