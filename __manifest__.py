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
        'security/security.xml',
        'security/ir.model.access.csv',
        'views/views.xml',
        'views/templates.xml',
        'views/openacademy.xml',
        'views/partner.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}
