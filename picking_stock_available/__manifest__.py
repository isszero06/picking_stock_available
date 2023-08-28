# -*- coding: utf-8 -*-
{
    'name': 'Available Qty during Picking',
    'version': '6.0.1',
    'category': 'Warehouse',
    "author": 'Zero Systems',
    "company": 'Zero for Information Systems',
    "website": "https://www.erpzero.com",
    "email": "sales@erpzero.com",
    "sequence": 0,

    'summary': """Show Not Reserved Stock Qty during Picking""",

    'description': """
            Show Not Reserved Stock Qty during Picking """,
    'depends': [
        'stock',
    ],
    'data': [
        'views/view.xml',
    ],
    'license': 'OPL-1',
    'live_test_url': 'https://youtu.be/sKpVr-vUcoA',
    'images': ['static/description/picking_stock_available.png'],
    'installable': True,
    'auto_install': False,
    'application': False,
    'price': 00.0,
    'currency': 'EUR',
    'pre_init_check_vers': 'pre_init_check_vers',
}
