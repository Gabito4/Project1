from exceptions.ressource_unavailable import ResourceUnavailable
from Models.classroom import Classroom
from repos.classroom_repo import ClassroomRepo
from repos.classroom_repo_temp import ClassroomRepoTemp
from time import time
from datetime import datetime


class ClassroomService:

    def __init__(self, classroom_repo: ClassroomRepo):
        self.classroom_repo = classroom_repo

    def create_classroom(self, classroom):
        return self.classroom_repo.create_classroom(classroom)

    def get_classroom_by_id(self, classroom_id):
        return self.classroom_repo.get_classroom(classroom_id)

    def get_all_classrooms(self):
        return self.classroom_repo.all_classrooms()

    def update_classroom(self, change):
        return self.classroom_repo.update_classroom(change)

    def delete_classroom(self, classroom_id):
        return self.classroom_repo.delete_classroom(classroom_id)

    def get_classroom_above_price(self, price):
        classrooms = self.get_all_classrooms()

        refined_search = []

        for classroom in classrooms:
            if classroom.price >= price:
                refined_search.append(classroom)

        return refined_search

    def checkout_classroom(self, classroom_id):
        classroom = self.get_classroom_by_id(classroom_id)
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
    cr: ClassroomRepo = ClassroomRepoTemp()
    crs: ClassroomService = ClassroomService(cr)

    print(crs.get_all_classrooms())

    print("---------")
    print(crs.get_classroom_above_price(4.5))
    print(crs.get_classroom_above_price(5))
    print(crs.get_classroom_above_price(7))

    print(int(time()))

    crs.checkout_classroom(1)
    print(crs.get_classroom_by_id(1))
    crs.checkin_classroom(1)
    print(crs.get_classroom_by_id(1))


if __name__ == '__main__':
    _test()
