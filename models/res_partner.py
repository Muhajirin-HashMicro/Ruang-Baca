from odoo import api, fields, models


class Anggota(models.Model):
    _inherit = 'res.partner'

    is_anggota = fields.Boolean(string ='Anggota Perpustakaan', default=False)
    is_penulis = fields.Boolean(string ='Penulis Buku Perpustakaan', default=False)
    is_publisher = fields.Boolean(string ='Publisher Buku Perpustakaan', default=False)
 