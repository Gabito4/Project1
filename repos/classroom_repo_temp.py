from exceptions.resource_not_found import ResourceNotFound
from Models.classroom import Classroom
from repos.classroom_repo import ClassroomRepo
from dbconnection.dataconnection import connection as data


class ClassroomRepoTemp(ClassroomRepo):

    def create_classroom(self, classroom):
        data.classroom[classroom.classroom_id] = classroom

    def get_classroom(self, classroom_id):
        try:
            return data.classroom[classroom_id]
        except KeyError:
            raise ResourceNotFound(f"Classroom with id: {classroom_id} - Not Found")

    def all_classrooms(self):
        classrooms = data.classroom.values()
        return [classroom for classroom in classrooms]

    def update_classroom(self, change):
        data.classroom.update({change.classroom_id: change})

    def delete_classroom(self, classroom_id):
        del data.classrooms[classroom_id]


def _test():
    cr = ClassroomRepoTemp()
    classroom1 = Classroom(classroom_id=4, title="Chemistry", price=896, grade=76, start_date=8282022)
    cr.create_classroom(classroom1)
    print(data.classrooms)

    classroom2 = cr.get_classroom(2)
    print(classroom2)

    print(cr.all_classrooms())

    classroom1.price += 1
    cr.update_classroom(classroom1)
    print(cr.all_classrooms())

    cr.delete_classroom(3)
    print(cr.all_classrooms())


if __name__ == '__main__':
    _test()
