""" This module creates a course model """

from odoo import models, fields


class Course(models.Model):
    _name = 'openacademy.course'
    _description = 'course'
    name = fields.Char(string="Title", required=True)
    description = fields.Text()
    responsible_id = fields.Many2one('res.users', string="Responsible", index=True)
    session_ids = fields.One2many("openacademy.session", "course_id", string="Sessions")
    _sql_constraints = [("different_attributes", "CHECK(name != description)"
                         , "Course title and description must be different"),
                        ("unique_coursename", "UNIQUE(name)", "Course title must be unique")]
