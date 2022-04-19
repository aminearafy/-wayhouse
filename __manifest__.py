# -*- coding: utf-8 -*-
{
    'name': 'WayHouse - Warehouse Management',
    'version': '0.1',
    'category': 'Inventory',
    'summary': 'WayHouse - Your Way to Manage your WareHouse',
    'sequence': '10',
    'license': 'AGPL-3',
    'author': 'WayHouse',
    'maintainer': 'WayHouse',
    'website': 'https://wayhouse.io',
    'depends': ['base', 'stock'],
    'installable': True,
    'application': True,
    'auto_install': False,
    'data': [
        'security/ir.model.access.csv',
        'security/security.xml',
        'views/wayhouse_product_template_views.xml',
        'views/format_list_views.xml',
        'views/format_views.xml',
        'views/choix_list_views.xml',
        'views/wayhouse_journal_prod_views.xml',
        'views/camion_list_views.xml',
        'views/cariste_list_views.xml',
        'views/chauffeur_list_views.xml',
        'report/production_report.xml',
        'report/production_template.xml',
        'report/production_details_template.xml',
    ],
    'assets': {
        'web.assets_backend': [
            #'wayhouse/static/src/js/qrcode/html5-qrcode.min.js',
            #'wayhouse/static/src/js/qrcode/qrcode.min.js',
            #'wayhouse/static/src/js/wayhouse/script.js',
        ],
    },
}
