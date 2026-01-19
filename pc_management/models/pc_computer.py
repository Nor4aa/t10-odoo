from odoo import models, fields, api
from odoo.exceptions import ValidationError
from datetime import date

class PcComputer(models.Model):
    _name = "pc.computer"
    _description = "Ordenador"

    name = fields.Char(string="Número de equipo", required=True)

    user_id = fields.Many2one(
        "res.users",
        string="Usuario"
    )

    component_ids = fields.Many2many(
        "pc.component",
        string="Componentes"
    )

    last_update = fields.Date(
        string="Última modificación"
    )

    total_price = fields.Monetary(
        string="Precio total",
        compute="_compute_total_price",
        store=True
    )

    notes = fields.Text(string="Incidencias")

    currency_id = fields.Many2one(
        "res.currency",
        string="Moneda",
        default=lambda self: self.env.company.currency_id
    )

    # restringir fecha
    @api.constrains("last_update")
    def _check_last_update(self):
        for record in self:
            if record.last_update and record.last_update > date.today():
                raise ValidationError("La fecha no puede ser futura")

    # -calculo del precio
    @api.depends("component_ids.price")
    def _compute_total_price(self):
        for record in self:
            total = 0
            for component in record.component_ids:
                total += component.price
            record.total_price = total
