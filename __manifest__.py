# -*- coding: utf-8 -*-
{
    'name': "openacademy",

    'summary': "Courses and sessions management module",

    'description' : "Courses and sessions management module",

    'author': "Dounia Bennoune",


    'category': 'Education',
    'version': '0.1',

    'depends': ['base','board'],

    'data': [
        'security/ir.model.access.csv',
        'security/security.xml',
        'data/data.xml',
        'views/course_view.xml',
        'views/session_view.xml',
        'views/partner_view.xml',
        'views/dashboard.xml',
        'wizard/session_wizard.xml',
        'reports/report.xml',
        'reports/session_details.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}
