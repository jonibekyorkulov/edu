from enum import Enum


class UserRol(Enum):
    ADMIN = "admin"
    TEACHER = "teacher"
    STUDENT = "student"


    @classmethod
    def choices(cls):
        return tuple((key.value, key.name) for key in cls)
    
class Gender(Enum):
    ERKAK = "erkak"
    AYOL = "ayol"

    @classmethod
    def choices(cls):
        return tuple((key.value, key.name) for key in cls)
    


    



