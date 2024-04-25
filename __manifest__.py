# -*- coding: utf-8 -*-
{
    'name': 'Theme Apexive',
    'version': '16.0.0.2',
    'category': 'Theme',
    'author': 'Ehtisham Faisal  ',
    'summary': 'Webflow Theme Converted into Odoo16.',
    'description': """
        This module is a conversion of Webflow Theme
        """,
    'website': 'https://github.com/ehtishamfaisal',
    'depends': ['base', 'website'],
    'data': [
        'views/header.xml',
        # 'views/footer.xml',
        # 'views/401.xml',
        # 'views/404.xml',
        # 'views/aboutus.xml',
    ],
    'demo': [],
    'icon': 'apexive_website//static/src/img/new-logo.svg',
    'images': [],
    'installable': True,
    'application': True,
    'license': 'LGPL-3',
    'assets': {
        'web.assets_frontend': [
            '/apexive_website/static/src/css/apexive.webflow.css',
            '/apexive_website/static/src/css/normalize.css',
            '/apexive_website/static/src/css/webflow.css',


            '/apexive_website/static/src/js/**/*',
        ],
    },
}
