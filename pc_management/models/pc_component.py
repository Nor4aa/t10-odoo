from odoo import models, fields

class PcComponent(models.Model):
    _name = "pc.component"
    _description = "Componente"

    name = fields.Char(string="Nombre", required=True)
    specs = fields.Text(string="Especificaciones")
    price = fields.Monetary(string="Precio")

    currency_id = fields.Many2one(
        "res.currency",
        string="Moneda",
        default=lambda self: self.env.company.currency_id
    )
