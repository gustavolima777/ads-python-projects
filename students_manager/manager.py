""" Classes for managing students, courses, and disciplines. """
import argparse
from models import Student, Subject, Course

class StudentsManager:
    def __init__(self, students: list[Student]):  
        self.students = students

    @classmethod
    def from_input(
        self,
        first: bool = False,
        ):
        student_name = input("Enter the student name: ")
        student_course = input("Enter the course name: ")
        student_subject = input("Enter the subject name: ")
        student_professor = input("Enter the professor name: ")
        student_grade = float(input("Enter the grade: "))
        student = Student(
                student_name,
                Course(
                    student_course,
                    [Subject(student_subject, student_professor, student_grade)],
                ),
            )
        if first:
            return self([student])
        else:
            raise ValueError(
                "This method can only initialize the manager for the first time. Use an instance method to add students."
            )

    @classmethod
    def from_dict(self, data: dict) -> None:
        students = []
        for students_info in data.get("students"):  
            student_name = students_info["name"]
            subjects = []
            for subject_name, infos in students_info["course"]["subjects"].items():  
                subjects.append(  
                    Subject(subject_name, infos["professor"], infos["grade"])  
                )
            course = Course(students_info["course"]["course_name"], subjects)
            students.append(Student(student_name, course))  
        return StudentsManager(students)
    
    def add_student_from_input(self):
        """add a student to the list of students from input"""
        student_name = input("Enter the student name: ")
        student_course = input("Enter the course name: ")
        student_subject = input("Enter the subject name: ")
        student_professor = input("Enter the professor name: ")
        student_grade = float(input("Enter the grade: "))
        student = Student(
            student_name,
            Course(
                student_course,
                [Subject(student_subject, student_professor, student_grade)],
            ),
        )
        self.students.append(student)

    def get_approved_course_students_list(self, min: float = 60) -> list[Student]:  
        return [student for student in self.students if student.approved(min)]
    
if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Students Manager")
    parser.add_argument(
            "-f", "--file", type=str, help="Path to the JSON file with students data"
        )
    args = parser.parse_args()
    if args.file:
        import json
        with open(args.file, "r") as file:
            data = json.load(file)
        manager = StudentsManager.from_dict(data)

    manager = StudentsManager.from_input(first=True)
    
    exit = None
    while exit != "exit":
        action= input("Enter the action (list, add): ")
        if action == "list":
            min_grade = float(input("Enter the minimum grade: "))
            approved_students = manager.get_approved_course_students_list(min_grade)
            for student in approved_students:
                print(f"Student: {student.name}, Course: {student.course.course_name}")
        elif action == "add":
            manager.add_student_from_input()
        else:
            print("Invalid action")
        exit = input("Type 'exit' to quit or press Enter to continue: ")        