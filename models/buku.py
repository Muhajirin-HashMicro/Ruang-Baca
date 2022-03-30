from odoo import api, fields, models


class Buku(models.Model):
    _name = 'perpus.buku'
    _description = 'Model Buku'

    name = fields.Char(string='Judul Buku')
    image = fields.Image('Image')
    stok = fields.Integer('Stok')
    penulis_id = fields.Many2one('res.partner', string='Penulis', domain=[('is_penulis', '=', True)])
    publisher_id = fields.Many2one('res.partner', string='Publisher', domain=[('is_publisher', '=', True)])
    tgl_publish = fields.Date('Tanggal Publish')
    kategori_ids = fields.Many2many('perpus.kategori', string='Kategori')
    rak_id = fields.Many2one('perpus.rak', string='Rak')
    
class Kategori(models.Model):
    _name = 'perpus.kategori'
    _description = 'Model Kategori'

    name = fields.Char(string='Nama Kategori')
    deskripsi = fields.Char(string='Deskripsi')

class Rak(models.Model):
    _name = 'perpus.rak'
    _description = 'Rak Buku'

    name = fields.Char(string='Nama Rak')
    lokasi = fields.Char(string='Lokasi')
    lantai = fields.Selection([
        ('lantai1', 'Lt. 1'),
        ('lantai2', 'Lt. 2'),
        ('lantai3', 'Lt. 3'),
        ('lantai4', 'Lt. 4'),
    ], string='Lantai')