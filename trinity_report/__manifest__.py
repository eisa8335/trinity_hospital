# -*- coding: utf-8 -*-
{
    'name': "Trinity Report",
    'summary': """
        A Form to record Reports information. This form is integrated with Patients and Doctors Form This form is a replica of a Report form provided by Cognito forms at https://www.cognitoforms.com/МаринГенчев/Report""",
    'description': """
        A Form to record Report information.
    """,
    'author': "Eisa Ahmed",
    'website': "https://www.fiverr.com/eisaahmed63",
    'category': 'Human Resources',
    'version': '16.0.1',
    'depends': ['base', 'trinity_patients', 'trinity_doctors_external', 'trinity_doctors', 'trinity_icd_diagnoses', 'trinity_insurance'],
    'data': [
        'security/ir.model.access.csv',
        'data/ir_sequence_data.xml',
        'data/ir_cron_data.xml',
        'data/data.xml',
        'views/views.xml'
    ],
    # 'assets': {
    #         'web.assets_backend': [
    #             'trinity_report/static/src/css/custom_css.css',
    #             'trinity_report/static/src/js/custom_js.js',
    #             # 'trinity_report/static/src/js/html2pdf_script.js',
    #             # 'trinity_report/static/src/js/jquery.min.js',
    #     ]
    # }
}
