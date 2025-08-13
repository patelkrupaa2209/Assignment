# -*- coding: utf-8 -*-
{
    'name': 'Partner Custom Features',
    'version': '17.0',
    'summary': 'Custom enhancements for partner and sale/delivery operations',
    'description': 'Module developed by Krupa as per assignment specification.',
    'author': 'Krupa',
    'category': 'Custom',
    'depends': ['base', 'sale_management', 'stock', 'mrp', 'purchase', 'purchase_stock'],
    'data': [
        'data/mail_template.xml',
        'data/automated_action.xml',
        'data/stock_picking_cron.xml',
        'views/stock_picking_views.xml',
        'views/sale_order_search_view.xml',
    ],
    'assets': {
        'web.assets_backend': [
            'partner_custom_features/static/src/js/clipboard_widget.js',
            'partner_custom_features/static/src/xml/clipboard_widget.xml',
        ],
    },
    'installable': True,
    'application': False,
}
