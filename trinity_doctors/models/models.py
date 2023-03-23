# -*- coding: utf-8 -*-

from odoo import models, fields, api, _
from odoo.exceptions import ValidationError


class TrinityDoctor(models.Model):
    _name = 'trinity.doctor'
    _description = 'Trinity Doctors'
    _rec_name = 'doctor_id'

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
    ], string='Identifier Type', required=True, default='personal_id', help='Select the Identification Method for the recorded person.')
    identifier = fields.Char()
    hospital_no = fields.Char(string='Hospital Number')
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

    # Defining Fields to store Specialization Information
    doctor_id = fields.Char(string='ID of Medical Doctor', required=True)
    speciality_id = fields.Many2one('doctor.speciality', string='NHIF Name')
    qualification_code_id = fields.Many2one('qualification.code', string='NHIF Code')
    attach = fields.Binary()
    attach_char = fields.Char(string="Medical Doctor Diploma")
    attach1 = fields.Binary()
    attach_char1 = fields.Char(string="Spetialty Diploma")
    attach2 = fields.Binary()
    attach_char2 = fields.Char(string="Medical Association Membership Certificate")
    attach3 = fields.Binary()
    attach_char3 = fields.Char(string="Contract Trinity MC")

    @api.onchange('speciality_id')
    def update_qualification_code(self):
        if self.speciality_id:
            rec = self.env['trinity.speciality'].search([('speciality_id', '=', self.speciality_id.id)])
            self.qualification_code_id = rec.qualification_code_id.id

    @api.onchange('qualification_code_id')
    def update_speciality(self):
        if self.qualification_code_id:
            rec = self.env['trinity.speciality'].search([('qualification_code_id', '=', self.qualification_code_id.id)])
            self.speciality_id = rec.speciality_id.id

    @api.constrains('doctor_id')
    def _restrict_duplicates(self):
        for rec in self:
            duplicates = self.env['trinity.doctor'].search(
                [('doctor_id', '=', rec.doctor_id), ('id', '!=', rec.id)])
            if duplicates:
                raise ValidationError(
                    _(f'Doctor ID {rec.doctor_id} is already used. Please enter a unique ID.'))
