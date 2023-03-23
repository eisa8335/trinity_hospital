# -*- coding: utf-8 -*-
{
    # Application Information
    'name': 'trinity_report_pdf',
    'version': '1.0',
    'category' : 'Human Resources',
    'description': """ 
        Trinity Reports Information in Pdf
    """,
    'summary': """
        Trinity Reports Information in Pdf
    """,

    # Author Information
    'author': 'Eisa Ahmed',
    # Technical Information
    'depends': ['base', 'trinity_report'],
    'data': [
        'views/template.xml',
        'views/module_report.xml',
    ],
}
