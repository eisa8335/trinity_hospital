# -*- coding: utf-8 -*-
{
    'name': "Trinity Patients",
    'summary': """
        A Form to record patients information. This form is a replica of a Patient form provided by Cognito forms at https://www.cognitoforms.com/%D0%9C%D0%B0%D1%80%D0%B8%D0%BD%D0%93%D0%B5%D0%BD%D1%87%D0%B5%D0%B2/Patient""",
    'description': """
        A Form to record patients information.
    """,
    'author': "Eisa Ahmed",
    'website': "https://www.fiverr.com/eisaahmed63",
    'category': 'Human Resources',
    'version': '16.0.1',
    'depends': ['base', 'trinity_insurance', 'trinity_doctors', 'trinity_doctors_external'],
    'data': [
        'security/ir.model.access.csv',
        'data/data.xml',
        'views/views.xml',
    ]
}
