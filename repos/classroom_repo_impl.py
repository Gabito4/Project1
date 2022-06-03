from exceptions.resource_not_found import ResourceNotFound
from Models.classroom import Classroom
from repos.classroom_repo import ClassroomRepo
from dbconnection.dataconnection import connection


def _build_classroom(record):
    if record:
        return Classroom(classroom_id=record[0], title=record[1], price=float(record[2]), start_date=record[3],
                         grade=(record[4] if record[4] else 0))
    else:
        return None


class ClassroomRepoImpl(ClassroomRepo):

    def create_classroom(self, classroom):
        sql = "INSERT INTO classrooms VALUES (DEFAULT,%s,%s,DEFAULT,NULL) RETURNING *"

        cursor = connection.cursor()
        cursor.execute(sql, [classroom.title, classroom.price])

        connection.commit()
        record = cursor.fetchone()

        return _build_classroom(record)

    def get_classroom(self, classroom_id):

        sql = "SELECT * FROM classrooms WHERE c_id = %s"
        cursor = connection.cursor()

        cursor.execute(sql, [classroom_id])

        record = cursor.fetchone()

        if record:
            return _build_classroom(record)
        else:
            raise ResourceNotFound(f"Classroom with id: {classroom_id} - Not Found")

    def all_classrooms(self):
        sql = "SELECT * FROM classrooms"
        cursor = connection.cursor()
        cursor.execute(sql)

        records = cursor.fetchall()

        classroom_list = [_build_classroom(record) for record in records]

        return classroom_list

    def update_classroom(self, change):
        sql = "UPDATE classrooms SET title=%s, price=%s, start_date=%s, course_id=%s WHERE c_id = %s  " \
              "RETURNING *"

        cursor = connection.cursor()
        cursor.execute(sql, [change.title, change.price,
                             change.start_date, (change.grade if change.grade > 0 else None), change.classroom_id])

        connection.commit()
        record = cursor.fetchone()

        return _build_classroom(record)

    def delete_classroom(self, classroom_id):
        sql = "DELETE FROM classrooms WHERE c_id = %s"

        cursor = connection.cursor()
        cursor.execute(sql, [classroom_id])
        connection.commit()


def _test():
    cr = ClassroomRepoImpl()
    classroom = cr.get_classroom(1)
    print(classroom)

    print(cr.all_classrooms())

    classroom = Classroom(title="Math 101", price=505)
    classroom = cr.create_classroom(classroom)
    print(cr.all_classrooms())
    print("-----------")
    classroom.title = "Math"
    classroom.price += 1
    classroom = cr.update_classroom(classroom)

    print(classroom)

    print("---SUCCESSFULLY DELETED---")
    cr.delete_classroom(classroom.classroom_id)
    print(cr.all_classrooms())


if __name__ == '__main__':
    _test()
