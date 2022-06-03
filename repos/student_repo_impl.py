from exceptions.resource_not_found import ResourceNotFound
from Models.student import Student
from Models.users import Users
from Models.tempdb import Tempdb
from repos.student_repo import StudentRepo
from dbconnection.dataconnection import connection


def _build_student(record):
    return Student(student_id=record[0], name=record[1], age=record[2], grade=record[3])


def _build_user(record):
    return Users(username=record[0], password=record[1], email=record[2], user_id=record[3], isadmin=record[4])


def _build_tempdb(record):
    return Tempdb(tempid=record[0], rmbavailable=record[1], rmbavailable2=record[2],
                 submission=record[3], usersubmissionid=record[4], alreadysubmitted=record[5])


class StudentRepoImpl(StudentRepo):
    def get_student(self, student_id):
        sql = "SELECT * FROM students WHERE s_id = %s"

        cursor = connection.cursor()
        cursor.execute(sql, [student_id])

        record = cursor.fetchone()

        if record:
            return _build_student(record)
        else:
            raise ResourceNotFound(f"Student with id: {student_id} - Not Found")

    def get_tempdata(self, temp_id):
        sql = "SELECT * FROM tempdatabase WHERE s_id = %s"

        cursor = connection.cursor()
        cursor.execute(sql, [temp_id])

        record = cursor.fetchone()

        if record:
            return _build_tempdb(record)
        else:
            raise ResourceNotFound(f"Student with id: {temp_id} - Not Found")

    def all_students(self):
        sql = "SELECT * FROM students"

        cursor = connection.cursor()
        cursor.execute(sql)

        records = cursor.fetchall()

        return [_build_student(record) for record in records]

    def all_tempdata(self):
        sql = "SELECT * FROM tempdatabase"

        cursor = connection.cursor()
        cursor.execute(sql)

        records = cursor.fetchall()

        return [_build_tempdb(record) for record in records]

    def get_user(self, user_id):
        sql = "SELECT * FROM loging_info WHERE user_id = %s"

        cursor = connection.cursor()
        cursor.execute(sql, [user_id])

        record = cursor.fetchone()

        if record:
            return _build_user(record)
        else:
            raise ResourceNotFound(f"User with id: {user_id} - Not Found")

    def all_users(self):
        sql = "SELECT * FROM loging_info"

        cursor = connection.cursor()
        cursor.execute(sql)

        records = cursor.fetchall()

        return [_build_user(record) for record in records]

    def get_student_from_classroom(self, classroom_id):
        sql = "SELECT students.* FROM studentclassroom " \
              "LEFT JOIN students ON studentclassroom.student_id = students.s_id " \
              "WHERE studentclassroom.classroom_id = %s"

        cursor = connection.cursor()
        cursor.execute(sql, [classroom_id])

        records = cursor.fetchall()
        return [_build_student(record) for record in records]

    def create_student(self, student):
        sql = "INSERT INTO students VALUES (DEFAULT,%s,%s,DEFAULT) RETURNING *"

        cursor = connection.cursor()
        cursor.execute(sql, [student.name, student.age])

        connection.commit()
        record = cursor.fetchone()

        return _build_student(record)

    def create_tempdb(self, tempdata):
        sql = "INSERT INTO tempdatabase VALUES (%s,%s,%s,%s,%s,%s) RETURNING *"

        cursor = connection.cursor()
        cursor.execute(sql, [tempdata.tempid, tempdata.rmbavailable, tempdata.rmbavailable2,
                             tempdata.submission, tempdata.usersubmissionid, tempdata.alreadysubmitted])

        connection.commit()
        record = cursor.fetchone()

        return _build_tempdb(record)

    def update_student(self, change):
        sql = "UPDATE students SET name=%s, age=%s, grade=%s, administrator=%s WHERE s_id = %s  " \
              "RETURNING *"

        cursor = connection.cursor()
        cursor.execute(sql, [change.title, change.age,
                             (change.grade if change.grade > 0 else None), change.administrator])

        connection.commit()
        record = cursor.fetchone()

        return _build_student(record)

    def delete_student(self, student_id):
        sql = "DELETE FROM students WHERE s_id = %s"

        cursor = connection.cursor()
        cursor.execute(sql, [student_id])
        connection.commit()


def _test():
    sri = StudentRepoImpl()
    print(sri.get_student(1))
    print(sri.all_students())
    print(sri.get_student_from_classroom(1))


if __name__ == '__main__':
    _test()
