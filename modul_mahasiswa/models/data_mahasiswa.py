from odoo import models, fields, api, _, exceptions
from odoo.exceptions import ValidationError

class DataMahasiswa(models.Model):
    _name = "data.mahasiswa"

    Nim = fields.Integer(string='NIM Mahasiswa') 
    name = fields.Char(string='Nama Mahasiswa')
    TglLahir = fields.Date(string='Tanggal Lahir')
    agama = fields.Selection([("1","Islam"),("2","Protestan"),("3","Katolik"),("4","Hindu"),("5","Budha"),("6","Konghucu")], string='Agama', default="1")
    jk = fields.Selection([("p","Pria"),("w","Wanita")], string='Jenis Kelamin')
    alamat = fields.Char(string='Alamat')