import unittest

from Models.classroom import Classroom
from repos.classroom_repo_impl import ClassroomRepoImpl

cr = ClassroomRepoImpl()


class TestClassroomRepo(unittest.TestCase):

    added_classroom = Classroom()

    def test_get_classroom_success(self):
        classroom = cr.get_classroom(1)
        self.assertEqual(classroom, Classroom(classroom_id=1, title="Biology",
                                              price=705, grade=91, start_date=8282022))

    def test_create_classroom_success(self):
        TestClassroomRepo.added_classroom = cr.create_classroom(self.added_classroom)

        self.assertEqual(self.added_classroom, Classroom(classroom_id=self.added_classroom.classroom_id, title="",
                                                         price=0, grade=0, start_date=0))

        self.assertIsNotNone(cr.get_classroom(self.added_classroom.classroom_id))
        print(self.added_classroom)

    @classmethod
    def tearDownClass(cls):
        if cls.added_classroom.classroom_id:
            cr.delete_classroom(cls.added_classroom.classroom_id)


if __name__ == '__main__':
    unittest.main()
