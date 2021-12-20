from odoo import fields, models


class Partner(models.Model):
    _inherit = "res.partner"

    instr = fields.Boolean(default=False,string="instructor",)
    Session_partner = fields.Many2many("session",string="Sessions")
