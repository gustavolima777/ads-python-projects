""" Models for the students manager application."""

class Subject:
    def __init__(self, name: str, professor: str, grade: float):
        self.name = name
        self.professor = professor
        self.grade = grade

    def approved(self, min: float = 60) -> bool:
        return self.grade >= min
    
class Course:
    def __init__(self, name: str, subjects: list[Subject]):
        self.course_name = name
        self.subjs = subjects

    def calculate_mean(self) -> float:
        return sum(d.grade for d in self.subjs) / len(self.subjs)

    def approved(self, min: float = 60) -> bool:
        return all(d.approved(min) for d in self.subjs)

class Student:
    def __init__(self, name: str, course: Course):
        self.name = name
        self.course = course

    def approved(self, min: float = 60) -> bool:
        return self.course.approved(min)
