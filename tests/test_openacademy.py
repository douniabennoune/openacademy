from odoo.tests.common import SavepointCase
from odoo.exceptions import ValidationError, UserError
import datetime


class OpenAcademyTest(SavepointCase):
    @classmethod
    def setUpClass(cls):
        super(OpenAcademyTest, cls).setUpClass()
        cls.course = cls.env['openacademy.course'].create([{'name': 'course_test', }])
        cls.session = cls.env['openacademy.session'].create([{'name': 'session test', 'course_id': cls.course.id,
                                                              'instructor_id': 52, 'attendees_ids': [52, 33, 27], }])

    def test_compute_taken_seats_null(self):
        self.session.number_of_seats = 0
        self.assertEqual(self.session.taken_seats, 0)

    def test_compute_taken_seats(self):
        self.session.number_of_seats = 20
        self.assertEqual(self.session.taken_seats, 15)

    def test_onchange_number_of_seats_negative(self):
        self.session.attendees_number = 3
        self.session.number_of_seats = -1
        res = self.session._onchange_number_of_seats()
        self.assertTrue('warning' in res)

    def test_onchange_number_of_seats(self):
        self.session.attendees_number = 3
        self.session.number_of_seats = 2
        res = self.session._onchange_number_of_seats()
        self.assertTrue('warning' in res)

    def test_compute_end_date_negative(self):
        with self.assertRaises(ValidationError):
            self.session.duration = -5
            self.session._compute_end_date()

    def test_compute_end_date(self):
        self.session.duration = 5
        self.assertEqual(self.session.end_date, datetime.date(2021, 12, 28))

    def test_get_attendees_number(self):
        self.assertEqual(self.session.attendees_number, 3)

    def test_check_presence_instructor(self):
        with self.assertRaises(ValidationError):
            self.session.attendees_ids = [27, 33]
            self.session._check_presence_instructor()
