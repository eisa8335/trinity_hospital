# -*- coding: utf-8 -*-

from odoo import models, fields, api


class TrinityInsurance(models.Model):
    _name = 'trinity.insurance'
    _description = 'Trinity Insurance'

    # Defining Fields to store Personal Information
    name = fields.Char(required=True)
    vat_number = fields.Char()

    # Contact Person Details
    first_name = fields.Char(string='Name of Contact Person', required=True)
    middle_name = fields.Char()
    last_name = fields.Char()
    email = fields.Char()
    phone = fields.Char()

    # Defining Fields to store Address Information
    address_line = fields.Char()
    address_line2 = fields.Char()
    city = fields.Char()
    state_id = fields.Many2one(comodel_name="res.country.state")
    zip_code = fields.Char()
    country_id = fields.Many2one(comodel_name='res.country')

    attach = fields.Binary()
    attach_char = fields.Char(string="Contract")
