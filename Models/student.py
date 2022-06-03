class Student:

    def __init__(self, student_id=0, name="", age=0, grade=0, administrator=0):
        self.student_id = student_id
        self.name = name
        self.age = age
        self.grade = grade
        self.administrator = administrator

    def __repr__(self):
        return str({
            "student_id": self.student_id,
            "name": self.name,
            "age": self.age,
            "grade": self.grade,
            "administrator": self.administrator
        })

    def json(self):
        return {
            "studentId": self.student_id,
            "name": self.name,
            "age": self.age,
            "grade": self.grade,
            "administrator": self.administrator
        }
