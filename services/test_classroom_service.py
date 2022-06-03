import unittest
from unittest.mock import MagicMock

from Models.classroom import Classroom
from repos.classroom_repo_impl import ClassroomRepoImpl
from services.classroom_service import ClassroomService


class TestClassroomService(unittest.TestCase):
    cr = ClassroomRepoImpl()
    crs = ClassroomService(cr)

    def test_get_classroom_above_price(self):
        self.crs.get_all_students = MagicMock(return_value=[
            Classroom(classroom_id=1, title="Math", price=901, grade=68),
            Classroom(classroom_id=2, title="Physics", price=602, grade=76),
            Classroom(classroom_id=3, title="Chemistry", price=753, grade=73)
        ])

        refined_classrooms = self.crs.get_classroom_above_price(4)
        print(refined_classrooms)

        self.assertListEqual(refined_classrooms, [
            Classroom(classroom_id=2, title="Physics", price=602, grade=76),
            Classroom(classroom_id=3, title="Chemistry", price=753, grade=73)
        ])


if __name__ == '__main__':
    unittest.main()
