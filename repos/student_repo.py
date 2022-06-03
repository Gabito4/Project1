from abc import ABC, abstractmethod


class StudentRepo(ABC):

    @abstractmethod
    def get_student(self, student_id):
        pass

    @abstractmethod
    def all_students(self):
        pass

    @abstractmethod
    def all_tempdata(self):
        pass

    @abstractmethod
    def create_tempdb(self, tempdata):
        pass

    @abstractmethod
    def get_student_from_classroom(self, classroom_id):
        pass
