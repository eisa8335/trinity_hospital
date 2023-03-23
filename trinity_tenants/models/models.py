# -*- coding: utf-8 -*-

from odoo import models, fields, api


class TrinityTenants(models.Model):
    _name = 'trinity.tenant'
    _description = 'Trinity Tenant'

    # Defining Fields to store Personal Information
    name = fields.Char(required=True)
    vat_number = fields.Char()

    # Contact Person Details
    first_name = fields.Char(string='Name of Contact Person', required=True)
    middle_name = fields.Char()
    last_name = fields.Char()
    email = fields.Char()
    phone = fields.Char()
    rent_due_date = fields.Date(string='Rent Due Date')
    rent = fields.Float()
    premisses = fields.Char()

    # Defining Fields to store Address Information
    address_line = fields.Char()
    address_line2 = fields.Char()
    city = fields.Char()
    state_id = fields.Many2one(comodel_name="res.country.state")
    zip_code = fields.Char()
    country_id = fields.Many2one(comodel_name='res.country')

    attach = fields.Binary()
    attach_char = fields.Char(string="Contract")
    attach1 = fields.Binary()
    attach_char1 = fields.Char(string="Contract")
    attach2 = fields.Binary()
    attach_char2 = fields.Char(string="Contract")
    attach3 = fields.Binary()
    attach_char3 = fields.Char(string="Contract")
    attach4 = fields.Binary()
    attach_char4 = fields.Char(string="Contract")
