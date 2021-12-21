from odoo import fields, models


class Partner(models.Model):
    _inherit = "res.partner"
    is_instructor = fields.Boolean(default=False, string="instructor")
    session_partners = fields.Many2many("openacademy.session", string="Sessions")
