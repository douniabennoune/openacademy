from odoo import models, fields, api


class SessionWizard(models.TransientModel):
    _name = "session.wizard"

    def _default_sessions(self):
        return self.env['session'].browse(self._context.get('active_ids'))

    session_ids = fields.Many2many("session", required=True, string="Session", default=_default_sessions)
    attendees = fields.Many2many("res.partner")

    def subscribe(self):
        for session in self.session_ids:
            session.attendees |= self.attendees
        return {}
