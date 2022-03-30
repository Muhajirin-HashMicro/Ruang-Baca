from odoo import api, fields, models
import datetime
from odoo.exceptions import ValidationError


class Peminjaman(models.Model):
    _name = 'perpus.peminjaman'
    _description = 'Model Peminjaman'

    name = fields.Char(string='Name')
    detailpeminjaman_ids = fields.One2many('perpus.detailpeminjaman', inverse_name='peminjaman_id', string='Detail Peminjaman')
    anggota_id = fields.Many2one('res.partner', string='Anggota Peminjam', domain=[('is_anggota', '=', True)])
    lamapinjam = fields.Integer('Lama Pinjam/Hari')
    tgl_pinjam = fields.Date('Tanggal Pinjam', default=fields.Date.today())
    tgl_kembali = fields.Date(compute='_compute_tgl_kembali', string='Tanggal Kembali', store=True)
    is_kembali = fields.Boolean('Sudah Kembali', deafult=False)
    
    @api.depends('lamapinjam')
    def _compute_tgl_kembali(self):
        for record in self:
            record.tgl_kembali = record.tgl_pinjam + datetime.timedelta(days=record.lamapinjam)
    

class DetailPeminjaman(models.Model):
    _name = 'perpus.detailpeminjaman'
    _description = 'Model Detail Peminjaman'

    name = fields.Char(string='Name')
    peminjaman_id = fields.Many2one('perpus.peminjaman', string='ID Peminjaman')
    buku_id = fields.Many2one('perpus.buku', string='ID Buku')
    qty = fields.Integer('qty', default=1)

    @api.constrains('qty')
    def _constrains_qty(self):
        for record in self:
            cek = self.env['perpus.buku'].search([('id', '=', record.buku_id.id),('stok', '<', record.qty)])
            if cek:
                raise ValidationError("Stok %s Tidak Cukup!" %record.buku_id.name)

    @api.model
    def create(self, vals):
        record = super(DetailPeminjaman, self).create(vals)
        if record.qty:
            self.env['perpus.buku'].search([('id', '=', record.buku_id.id)]).write({'stok':record.buku_id.stok-record.qty})
            return record

    


