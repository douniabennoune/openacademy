from datetime import timedelta
from odoo import models, fields, api
from odoo.exceptions import ValidationError


class Session(models.Model):
    _name = 'openacademy.session'
    _description = 'session'
    name = fields.Char(string="Title", required=True)
    start_date = fields.Date(string="Start date", default=lambda self: fields.Date.today())
    duration = fields.Float(string="Duration")
    number_of_seats = fields.Integer(string="Number of seats")
    instructor_id = fields.Many2one("res.partner", string="Instructor",
                                    domain=['|', ('is_instructor', '=', True),
                                            ('category_id', 'ilike', 'Teacher')])
    course_id = fields.Many2one("openacademy.course", ondelete='cascade', string="course", required=True)
    attendees_ids = fields.Many2many("res.partner", string="Attendees")
    active = fields.Boolean(default=True, string="Active")
    taken_seats = fields.Float(string="Taken seats", compute="_compute_taken_seats")
    end_date = fields.Date(string="End date", compute="_compute_end_date")
    attendees_number = fields.Integer(compute="_get_attendees_number", store=True)

    @api.depends('attendees_ids', 'number_of_seats')
    def _compute_taken_seats(self):
        for record in self:
            if not record.number_of_seats:
                record.taken_seats = 0
            else:
                record.taken_seats = (len(record.attendees_ids) / record.number_of_seats) * 100

    @api.depends('start_date', 'duration')
    def _compute_end_date(self):
        for record in self:
            if self.duration < 0:
                raise ValidationError("The duration should not be negative")
            else:
                record.end_date = record.start_date + timedelta(days=record.duration)

    @api.depends('attendees_ids')
    def _get_attendees_number(self):
        for record in self:
            record.attendees_number = len(record.attendees_ids)

    @api.onchange('number_of_seats', 'attendees_ids')
    def _onchange_number_of_seats(self):
        res = {}
        if self.number_of_seats < 0:
            res['warning'] = {'title': "Error",'message': 'Number of seats cannot be negative'}
            return res

        if len(self.attendees_ids) > self.number_of_seats:
            res['warning'] = {'title': "Error", 'message': 'Number of attendees is bigger than the number of seats'}
            return res

    @api.constrains('instructor_id', 'attendees_ids')
    def _check_presence_instructor(self):
        for record in self:
            if record.instructor_id not in record.attendees_ids:
                raise ValidationError("The instructor is not present in the attendees list")
