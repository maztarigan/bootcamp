from odoo import models, fields, api, _, exceptions
from odoo.exceptions import ValidationError

class ProductAttrib(models.Model):
    _inherit = "product.template"

    density = fields.Integer(string='Density')