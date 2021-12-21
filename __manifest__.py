# -*- coding: utf-8 -*-
{
    'name': "openacademy",

    'summary': "Courses and sessions management module",

    'description' : "Courses and sessions management module",

    'author': "Dounia Bennoune",


    'category': 'Education',
    'version': '0.1',

    'depends': ['base'],

    'data': [
        'security/ir.model.access.csv',
        'security/security.xml',
        'data/data.xml',
        'views/course_view.xml',
        'views/session_view.xml',
        'views/partner_view.xml',
        'wizard/session_wizard.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}
