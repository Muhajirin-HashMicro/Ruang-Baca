# -*- coding: utf-8 -*-
{
    'name': "ruangbuku",

    'summary': """
        Short (1 phrase/line) summary of the module's purpose, used as
        subtitle on modules listing or apps.openerp.com""",

    'description': """
        Long description of module's purpose
    """,

    'author': "My Company",
    'website': "http://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/14.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Administration',
    'version': '1.0',
    'Application': True,

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'views/views.xml',
        'views/templates.xml',
        'views/menu.xml',
        'views/buku.xml',
        'views/kategori.xml',
        'views/rak.xml',
        'views/peminjaman.xml',
        'views/pengembalian.xml',
        'views/anggota.xml',
        'views/penulis.xml',
        'views/publisher.xml',
        'reports/report.xml',
        'reports/peminjaman_report.xml',
        'reports/pengembalian_report.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}
