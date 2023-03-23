# -*- coding: utf-8 -*-

from odoo import models, fields, api, _
from odoo.exceptions import ValidationError


class TrinitySpeciality(models.Model):
    _name = 'trinity.speciality'
    _description = 'Trinity Speciality'
    _rec_name = 'key'

    key = fields.Char(required=True)
    description_en = fields.Text(string='Description (En)')
    description_bg = fields.Text(string='Description (Bg)')
    role_healthcare = fields.Char(string='Role in Healthcare')
    speciality_id = fields.Many2one('doctor.speciality', string='NHIF Name')
    qualification_code_id = fields.Many2one('qualification.code', string='NHIF Code')

    @api.constrains('speciality_id', 'qualification_code_id')
    def _restrict_duplicates(self):
        for rec in self:
            if rec.qualification_code_id:
                duplicates = self.env['trinity.speciality'].search(
                    [('speciality_id', '=', rec.speciality_id.id), ('qualification_code_id', '!=', rec.qualification_code_id.id), ('id', '!=', rec.id)])
                if duplicates:
                    raise ValidationError(
                        _(f'Speciality Code {rec.speciality_id.name} is already used. Please enter a unique Code.'))
            if rec.speciality_id:
                duplicate_name = self.env['trinity.speciality'].search(
                    [('qualification_code_id', '=', rec.qualification_code_id.id), ('speciality_id', '!=', rec.speciality_id.id), ('id', '!=', rec.id)])
                if duplicate_name:
                    raise ValidationError(
                        _(f'NHIF Code {rec.qualification_code_id.name} is already used. Please enter a unique Code.'))


class NHIFName(models.Model):
    _name = 'doctor.speciality'
    _description = 'NHIF Name'

    name = fields.Char(required=True)


class NHIFCode(models.Model):
    _name = 'qualification.code'
    _description = 'NHIF Code'

    name = fields.Char(required=True)
