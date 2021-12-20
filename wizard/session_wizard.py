from odoo import models, fields, api
from odoo.exceptions import ValidationError
from datetime import timedelta, time


class SessionWizard(models.TransientModel):
    _name = "session.wizard"



