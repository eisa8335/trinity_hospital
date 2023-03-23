# -*- coding: utf-8 -*-
{
    'name': "Trinity ICD Diagnoses",
    'summary': """
        A Form to record ICD information. This form is a replica of a Doctor form provided by Cognito forms at https://www.cognitoforms.com/%D0%9C%D0%B0%D1%80%D0%B8%D0%BD%D0%93%D0%B5%D0%BD%D1%87%D0%B5%D0%B2/ICDDiagnoses""",
    'description': """
        A Form to record ICD information.
    """,
    'author': "Eisa Ahmed",
    'website': "https://www.fiverr.com/eisaahmed63",
    'category': 'Human Resources',
    'version': '16.0.1',
    'depends': ['base'],
    'data': [
        'security/ir.model.access.csv',
        'data/icd.diagnoses.csv',
        'views/views.xml'
    ]
}
