# -*- coding: utf-8 -*-

from odoo import models, fields, api, _
from odoo.exceptions import ValidationError


class TrinityDrug(models.Model):
    _name = 'trinity.drug'
    _description = 'Drugs'
    _rec_name = 'permit_number'

    # Defining Fields to store Drug Information
    key = fields.Char(string='Key')
    permit_number = fields.Char(string='Permit Number', required=True)
    inn_code = fields.Char(string='INN Code')
    atc_code = fields.Char(string='ATC Code')
    permit_owner = fields.Char(string='Permit Owner')
    package = fields.Char(string='Package')
    amount_active = fields.Char(string='Amount of Active Substance')
    measurement_unit_id = fields.Many2one(comodel_name="measurement.unit", string='Measurement Unit')
    medical_form_id = fields.Char(string='Medicinal Form ID')
    medicinal_form_id = fields.Many2one(comodel_name='medicinal.form', string='Medicinal Form')
    application_id = fields.Many2one(comodel_name='application.form', string='Application')

    @api.constrains('permit_number')
    def _restrict_duplicates(self):
        for rec in self:
            duplicates = self.env['trinity.drug'].search(
                [('permit_number', '=', rec.permit_number), ('id', '!=', rec.id)])
            if duplicates:
                raise ValidationError(
                    _(f'Permit No. {rec.permit_number} is already used. Please enter a unique Permit No.'))


class MeasurementUnit(models.Model):
    _name = 'measurement.unit'
    _description = 'Measurement Unit'

    name = fields.Char(required=True)


class MedicinalForm(models.Model):
    _name = 'medicinal.form'
    _description = 'Medicinal Form'

    name = fields.Char(required=True)


class ApplicationForm(models.Model):
    _name = 'application.form'
    _description = 'Application Form'

    name = fields.Char(required=True)
