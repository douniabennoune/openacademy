from odoo import models, fields, api


class Course(models.Model):
    _name = 'course'

    title = fields.Char(string="Title", required=True)
    description = fields.Text()

    responsible_id = fields.Many2one('res.users', ondelete="set null", string="Responsible", index=True)
    session_id = fields.One2many("session", "course_id", string="Sessions")

    _sql_constraints = [('different_attributes','CHECK(title!=description)','Course title and description must be different'),
                        ('unique_coursename','UNIQUE(title)','Course title must be unique')]


