# -*- coding: utf-8 -*-

from odoo import models, fields, api, _
from odoo.exceptions import ValidationError


class Patient(models.Model):
    _name = 'patient.patient'
    _description = 'Patients'
    _rec_name = 'identifier'

    # Defining Fields to store Personal Information
    title = fields.Selection(selection=[
        ('mr', 'Mr.'),
        ('mrs', 'Mrs.'),
        ('dr', 'Dr.'),
        ('prof', "Prof.")
    ], required=True, default='mr', help='Select the title of the person.')
    first_name = fields.Char(string='Name', required=True)
    middle_name = fields.Char()
    last_name = fields.Char()
    email = fields.Char()
    phone = fields.Char()
    identifier_type = fields.Selection(selection=[
        ('personal_id', 'Personal ID'),
        ('personal_foreigner_id', 'Personal Foreigner ID'),
        ('social_security_no', 'Social Security Number'),
        ('passport_no', "Passport Number"),
        ('other_type', "Other Type"),
        ('newborn_id', "Newborn ID"),
    ], string='Identifier Type', required=True, default='personal_id',
        help='Select the Identification Method for the recorded person.')
    identifier = fields.Char(required=True)
    birth_date = fields.Date(string='Birth Date', required=True)
    gender = fields.Selection(selection=[
        ('male', 'Male'),
        ('female', 'Female')
    ], required=True, default='male')

    # Defining Fields to store Address Information
    address_line = fields.Char()
    address_line2 = fields.Char()
    city = fields.Char()
    state_id = fields.Many2one(comodel_name="res.country.state")
    zip_code = fields.Char()
    country_id = fields.Many2one(comodel_name='res.country')

    # Defining Fields to store Insurance Related Information
    primary_insurance = fields.Many2one('trinity.insurance', string='Primary insurance', required=True)
    primary_insurance_no = fields.Char(string='Primary Insurance Number')
    secondary_insurance = fields.Many2one('trinity.insurance', string='Secondary insurance', required=True)
    secondary_insurance_no = fields.Char(string='Secondary Insurance Number')
    health_region_id = fields.Many2one('health.region', string='Health Region')
    health_region_no = fields.Char(string='Health Region Number')

    # General Practitioner
    general_practitioner_id = fields.Many2one('trinity.doctor.external', string='General Practitioner ID', required=True)
    general_practitioner_title = fields.Selection(selection=[
        ('mr', 'Mr.'),
        ('mrs', 'Mrs.'),
        ('dr', 'Dr.'),
        ('prof', "Prof.")
    ], help='Select the title of the person.', related='general_practitioner_id.title', store=True)
    general_practitioner_first_name = fields.Char(string='Name', related='general_practitioner_id.first_name', store=True)
    general_practitioner_middle_name = fields.Char(related='general_practitioner_id.middle_name', store=True)
    general_practitioner_last_name = fields.Char(related='general_practitioner_id.last_name', store=True)
    general_practitioner_email = fields.Char(related='general_practitioner_id.email', store=True)
    general_practitioner_phone = fields.Char(related='general_practitioner_id.phone', store=True)
    general_practitioner_identifier_type = fields.Selection(selection=[
        ('personal_id', 'Personal ID'),
        ('personal_foreigner_id', 'Personal Foreigner ID'),
        ('social_security_no', 'Social Security Number'),
        ('passport_no', "Passport Number"),
        ('other_type', "Other Type"),
        ('newborn_id', "Newborn ID"),
    ], string='Identifier Type',
        help='Select the Identification Method for the recorded person.', related='general_practitioner_id.identifier_type', store=True)
    general_practitioner_identifier = fields.Char(related='general_practitioner_id.identifier', store=True)
    general_practitioner_hospital_no = fields.Char(string='Hospital Number', related='general_practitioner_id.hospital_no', store=True)
    general_practitioner_birth_date = fields.Date(string='Birth Date', related='general_practitioner_id.birth_date', store=True)
    general_practitioner_gender = fields.Selection(selection=[
        ('male', 'Male'),
        ('female', 'Female')
    ], related='general_practitioner_id.gender', store=True)

    # Defining Fields to store Address Information
    general_practitioner_address_line = fields.Char(related='general_practitioner_id.address_line', store=True)
    general_practitioner_address_line2 = fields.Char(related='general_practitioner_id.address_line2', store=True)
    general_practitioner_city = fields.Char(related='general_practitioner_id.city', store=True)
    general_practitioner_state_id = fields.Many2one(comodel_name="res.country.state", related='general_practitioner_id.state_id', store=True)
    general_practitioner_zip_code = fields.Char(related='general_practitioner_id.zip_code', store=True)
    general_practitioner_country_id = fields.Many2one(comodel_name='res.country', related='general_practitioner_id.country_id', store=True)

    general_practitioner_speciality_id = fields.Many2one('doctor.speciality', string='NHIF Name', related='general_practitioner_id.speciality_id', store=True)
    general_practitioner_qualification_code_id = fields.Many2one('qualification.code', string='NHIF Code', related='general_practitioner_id.qualification_code_id', store=True)

    @api.constrains('identifier')
    def _restrict_duplicates(self):
        for rec in self:
            duplicates = self.env['patient.patient'].search(
                [('identifier', '=', rec.identifier), ('id', '!=', rec.id)])
            if duplicates:
                raise ValidationError(
                    _(f'Identifier {rec.identifier} is already used. Please enter a unique Identifier.'))

    # def name_get(self):
    #     """
    #     This function allows us to modify the name we will be showing for this model in a relational field
    #     """
    #     result = []
    #     for rec in self:
    #         name = f"{rec.identifier} {rec.first_name}"
    #         result.append((rec.id, name))
    #     return result


class HealthRegion(models.Model):
    _name = 'health.region'
    _description = 'Health Region'

    name = fields.Char(required=True)
