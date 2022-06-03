class Classroom:

    def __init__(self, classroom_id=0, title="", grade=0, price=0, start_date=0):
        self.classroom_id = classroom_id
        self.title = title
        self.grade = grade
        self.price = price
        self.start_date = start_date

    def __repr__(self):
        return str({
            'classroom_id': self.classroom_id,
            'title': self.title,
            'grade': self.grade,
            'price': self.price,
            'start_date': self.start_date
        })

    def json(self):
        return {
            'classroomId': self.classroom_id,
            'title': self.title,
            'grade': self.grade,
            'price': self.price,
            'StartDate': self.start_date
        }

    def __eq__(self, other):
        if not other:
            return False

        if not isinstance(other, Classroom):
            return False
        return self.__dict__ == other.__dict__


def _test():
    classroom1 = Classroom()
    classroom2 = Classroom()

    print(classroom1 == classroom2)

    classroom1 = Classroom(title="Math", price=701)
    classroom2 = Classroom(title="Math", price=701)

    print(classroom1 == classroom2)


if __name__ == '__main__':
    _test()

