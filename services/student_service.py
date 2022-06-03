from repos.student_repo import StudentRepo
from exceptions.ressource_unavailable import ResourceUnavailable
from Models.classroom import Classroom
from repos.classroom_repo import ClassroomRepo
from repos.classroom_repo_temp import ClassroomRepoTemp
from time import time
from datetime import datetime
from repos.student_repo_impl import StudentRepoImpl


class StudentService:

    def __init__(self, student_repo: StudentRepoImpl):
        self.student_repo = student_repo

    def all_students_in_classroom(self, classroom_id):
        return self.student_repo.get_student_from_classroom(classroom_id)

    def student_in_classroom(self, classroom_id, student_id):
        pass

    def create_student(self, student):
        return self.student_repo.create_student(student)

    # def create_student(self, student):
    #    return self.student_repo.create_student(student)

    def create_tempdb(self, tempdata):
        return self.student_repo.create_tempdb(tempdata)

    def get_student_by_id(self, student_id):
        return self.student_repo.get_student(student_id)

    def get_tempdata_by_id(self, student_id):
        return self.student_repo.get_student(student_id)

    def get_user_by_id(self, user_id):
        return self.student_repo.get_user(user_id)

    def get_all_tempdata(self):
        return self.student_repo.all_tempdata()

    def get_all_students(self):
        return self.student_repo.all_students()

    def get_all_users(self):
        return self.student_repo.all_users()

    def update_student(self, change):
        return self.student_repo.update_student(change)

    def delete_student(self, student_id):
        return self.student_repo.delete_student(student_id)

#    def get_classroom_above_price(self, price):
#        classrooms = self.get_all_classrooms()

 #  refined_search = []

        # for classroom in classrooms:
         #   if classroom.price >= price:
          #      refined_search.append(classroom)

        # return refined_search

    def checkout_classroom(self, student_id):
        classroom = self.get_classroom_by_id(student_id)
        if classroom.available:
            classroom.available = False
            classroom.start_date = int(time()) + 604800
            self.update_classroom(classroom)
            return classroom
        else:
            raise ResourceUnavailable(f"Classroom is unavailable. Expected start date: "
                                      f"{datetime.fromtimestamp(classroom.start_date)}")

    def checkin_classroom(self, classroom_id):
        classroom = self.get_classroom_by_id(classroom_id)
        if not classroom.available:
            classroom.available = True
            classroom.start_date = 0
            self.update_classroom(classroom)
            return classroom
        else:
            raise ResourceUnavailable(f"Classroom is full. Cannot register.")

    def _test():
        sr: StudentRepoImpl = StudentRepoImpl()
        sts: StudentService = StudentService(sr)

        print(sts.get_all_students())

        print("---------")

        #print(int(time()))

        print(sts.get_student_by_id(1))

        print(sts.get_student_by_id(1))

