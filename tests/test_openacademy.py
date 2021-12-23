from odoo.tests.common import TransactionCase
from odoo import fields
from odoo.exceptions import ValidationError


class SessionTest(TransactionCase):
    @classmethod
    def setUpClass(cls):
        super(SessionTest, cls).setUpClass()
        cls.course = cls.env['openacademy.course'].create([{'name': 'course_test'}])
        cls.session = cls.env['openacademy.session'].create([{'name': 'session 1', 'course_id': 'course_test'}])


    def test_create_course(self):
