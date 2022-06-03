from abc import ABC, abstractmethod


class ClassroomRepo(ABC):

    @abstractmethod
    def create_classroom(self, classroom):
        pass

    @abstractmethod
    def get_classroom(self, classroom_id):
        pass

    @abstractmethod
    def all_classrooms(self):
        pass

    @abstractmethod
    def update_classroom(self, change):
        pass

    @abstractmethod
    def delete_classroom(self, classroom_id):
        pass
