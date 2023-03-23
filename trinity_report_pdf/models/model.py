# -*- coding:utf-8 -*-


from odoo import models, fields, api


class ReportPDF(models.AbstractModel):
    _name = 'report.trinity_report_pdf.print_report'
    _description = "Report PDF"

    @api.model
    def _get_report_values(self, docids, data=None):

        record = self.env['trinity.report'].browse(docids)
        company = self.env['res.company'].search([('id', '=', 1)])

        return {
            'doc_ids': docids,
            'doc_model': 'trinity.report',
            'data': data,
            'docs': record,
            'company': company,
        }
