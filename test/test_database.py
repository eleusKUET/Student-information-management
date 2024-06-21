import unittest
import sqlite3
from modules.database import Database, initialize_database
import os

class TestDatabase(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        initialize_database(r'C:\Users\Eleus Ahammad\PycharmProjects\student-info-system\db\student_info_system_test.db')

    def setUp(self):
        self.db = Database(r'C:\Users\Eleus Ahammad\PycharmProjects\student-info-system\db\student_info_system_test.db')

    def test_add_student(self):
        self.db.add_student(StudentId=20202, Name='Alice', EnrollmentYear=2020, Major='Computer Science', Gender='Female', Age=20, Region='USA', test_Score=90)
        student = self.db.find_student(StudentId=20202)
        self.assertIsNotNone(student)
        self.assertEqual(student[1], 'Alice')

    def test_update_student(self):
        self.db.update_student(StudentId=20202, Name='Bob')
        student = self.db.find_student(StudentId=20202)
        self.assertIsNotNone(student)
        self.assertEqual(student[1], 'Bob')

    def tearDown(self):
        self.db.close()
    @classmethod
    def tearDownClass(cls):
        pass

database_file_path = r'C:\Users\Eleus Ahammad\PycharmProjects\student-info-system\db\student_info_system_test.db'
if os.path.exists(database_file_path):
    os.remove(database_file_path)


if __name__ == '__main__':
    unittest.main()
