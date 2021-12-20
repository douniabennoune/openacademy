from odoo import models, fields, api
from odoo.exceptions import ValidationError
from datetime import timedelta, time


class Session(models.Model):
    _name = 'session'

    name = fields.Char(string="Title", required=True)
    start_date = fields.Date(String="Start date", default=lambda self: fields.Date.today())
    duration = fields.Float()
    number_of_seats = fields.Integer(string="Number of seats")

    instructor_id = fields.Many2one("res.partner", string="Instructor",
                                    domain=['|', ('instr', '=', True), ('category_id', 'ilike', 'Teacher')])
    course_id = fields.Many2one("course", onedelete='cascade', string="course", required=True)

    attendees = fields.Many2many("res.partner")

    active = fields.Boolean(default=True)

    taken_seats = fields.Float(string="Taken seats", compute="_compute_taken_seats")

    end_date = fields.Date(String="End date", compute="_compute_end_date")

    attendees_number = fields.Integer(compute="_get_attendees_number",store=True)

    @api.depends('attendees', 'number_of_seats')
    def _compute_taken_seats(self):
        for record in self:
            if not record.number_of_seats:
                record.taken_seats = 0
            else:
                record.taken_seats = (len(record.attendees) / record.number_of_seats) * 100

    @api.depends('start_date', 'duration')
    def _compute_end_date(self):
        for record in self:
            record.end_date = record.start_date + timedelta(days=record.duration)

    @api.depends('attendees')
    def _get_attendees_number(self):
        for record in self:
            record.attendees_number = len(record.attendees)

    @api.onchange('number_of_seats', 'attendees')
    def _onchange_number_of_seats(self):
        if self.number_of_seats < 0:
            return {
                'warning': {
                    'title': "Error",
                    'message': 'Number of seats cannot be negative', },
            }

        if len(self.attendees) > self.number_of_seats:
            return {
                'warning': {
                    'title': "Error",
                    'message': 'Number of attendees is bigger than the number of seats'},
            }

    @api.constrains('instructor_id', 'attendees')
    def _check_presence_instructor(self):
        for record in self:
            if record.instructor_id not in record.attendees:
                raise ValidationError("The instructor is not present in the attendees list")
