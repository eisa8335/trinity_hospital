# -*- coding: utf-8 -*-

from odoo import models, fields, api


class TrinityICDDiagnosis(models.Model):
    _name = 'icd.diagnoses'
    _description = 'ICD Diagnoses'
    _rec_name = 'icd_code'

    # Defining Fields to store ICD Information
    icd_code = fields.Char(string='ICD Code', required=True)
    diagnosis_bulgarian = fields.Text(string='Diagnosis Bulgarian')
    diagnosis_english = fields.Text(string='Diagnosis English')
