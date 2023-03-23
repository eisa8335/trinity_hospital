# -*- coding: utf-8 -*-
{
    'name': "Trinity Doctors External",
    'summary': """
        A Form to record external doctors information. This form is a replica of a Doctor form provided by Cognito forms at https://www.cognitoforms.com/МаринГенчев/Doctors""",
    'description': """
        A Form to record external doctors information.
    """,
    'author': "Eisa Ahmed",
    'website': "https://www.fiverr.com/eisaahmed63",
    'category': 'Human Resources',
    'version': '16.0.1',
    'depends': ['base', 'trinity_doctors', 'trinity_specialty'],
    'data': [
        'security/ir.model.access.csv',
        'views/views.xml',
    ]
}
