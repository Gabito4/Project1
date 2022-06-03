# This is temporary code I am show you as a way to have functionality without worrying
# about data persistence quite yet.
from Models.classroom import Classroom


class TempDB:
    classrooms = {
        1: Classroom(classroom_id=1, title="Math", grade=98, price=505, start_date=8282022),
        2: Classroom(classroom_id=2, title="Physics", grade=86, price=405, start_date=8282022),
        3: Classroom(classroom_id=3, title="Biology", grade=74, price=489, start_date=8282022)
    }
