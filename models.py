"""
College Management & Student Admission System - Models (OOP Core Concepts)
"""

class Person:
    """Base class for individuals in the college system (Encapsulation & Abstraction)"""
    def __init__(self, person_id, name, email, phone, gender):
        self.person_id = person_id
        self.name = name
        self.email = email
        self.phone = phone
        self.gender = gender

    def get_details(self):
        return {
            "ID": self.person_id,
            "Name": self.name,
            "Email": self.email,
            "Phone": self.phone,
            "Gender": self.gender
        }


class Student(Person):
    """Derived Student class inheriting from Person (Inheritance & Polymorphism)"""
    def __init__(self, person_id, name, email, phone, gender, degree, department, year=1, fee_paid=0.0):
        super().__init__(person_id, name, email, phone, gender)
        self.degree = degree          # B.Tech / M.Tech
        self.department = department  # CSE, AI & ML, ECE, IT, ME
        self.year = year
        self.fee_paid = fee_paid
        self.enrolled_courses = []
        self.grades = {}              # Course -> Grade
        self.attendance = {}          # Course -> Percentage

    def get_details(self):
        base_details = super().get_details()
        base_details.update({
            "Degree": self.degree,
            "Department": self.department,
            "Year": f"Year {self.year}",
            "Fee Paid": f"₹{self.fee_paid:,.2f}",
            "Courses Count": len(self.enrolled_courses)
        })
        return base_details

    def to_dict(self):
        return {
            "person_id": self.person_id,
            "name": self.name,
            "email": self.email,
            "phone": self.phone,
            "gender": self.gender,
            "degree": self.degree,
            "department": self.department,
            "year": self.year,
            "fee_paid": self.fee_paid,
            "enrolled_courses": self.enrolled_courses,
            "grades": self.grades,
            "attendance": self.attendance
        }

    @classmethod
    def from_dict(cls, data):
        student = cls(
            person_id=data["person_id"],
            name=data["name"],
            email=data["email"],
            phone=data["phone"],
            gender=data["gender"],
            degree=data["degree"],
            department=data["department"],
            year=data.get("year", 1),
            fee_paid=data.get("fee_paid", 0.0)
        )
        student.enrolled_courses = data.get("enrolled_courses", [])
        student.grades = data.get("grades", {})
        student.attendance = data.get("attendance", {})
        return student


class Faculty(Person):
    """Derived Faculty class inheriting from Person"""
    def __init__(self, person_id, name, email, phone, gender, department, designation, salary):
        super().__init__(person_id, name, email, phone, gender)
        self.department = department
        self.designation = designation
        self.salary = salary
        self.assigned_courses = []

    def get_details(self):
        base_details = super().get_details()
        base_details.update({
            "Department": self.department,
            "Designation": self.designation,
            "Salary": f"₹{self.salary:,.2f}"
        })
        return base_details

    def to_dict(self):
        return {
            "person_id": self.person_id,
            "name": self.name,
            "email": self.email,
            "phone": self.phone,
            "gender": self.gender,
            "department": self.department,
            "designation": self.designation,
            "salary": self.salary,
            "assigned_courses": self.assigned_courses
        }

    @classmethod
    def from_dict(cls, data):
        faculty = cls(
            person_id=data["person_id"],
            name=data["name"],
            email=data["email"],
            phone=data["phone"],
            gender=data["gender"],
            department=data["department"],
            designation=data["designation"],
            salary=data["salary"]
        )
        faculty.assigned_courses = data.get("assigned_courses", [])
        return faculty


class Course:
    """Course representation"""
    def __init__(self, course_code, course_name, credits, semester, department):
        self.course_code = course_code
        self.course_name = course_name
        self.credits = credits
        self.semester = semester
        self.department = department

    def to_dict(self):
        return {
            "course_code": self.course_code,
            "course_name": self.course_name,
            "credits": self.credits,
            "semester": self.semester,
            "department": self.department
        }

    @classmethod
    def from_dict(cls, data):
        return cls(
            course_code=data["course_code"],
            course_name=data["course_name"],
            credits=data["credits"],
            semester=data["semester"],
            department=data["department"]
        )


class SeniorReview:
    """Senior Student Reviews and Campus Insights"""
    def __init__(self, reviewer_name, degree, department, passout_year, rating, review_text, company_placed):
        self.reviewer_name = reviewer_name
        self.degree = degree
        self.department = department
        self.passout_year = passout_year
        self.rating = rating          # 1 - 5 stars
        self.review_text = review_text
        self.company_placed = company_placed

    def to_dict(self):
        return {
            "reviewer_name": self.reviewer_name,
            "degree": self.degree,
            "department": self.department,
            "passout_year": self.passout_year,
            "rating": self.rating,
            "review_text": self.review_text,
            "company_placed": self.company_placed
        }

    @classmethod
    def from_dict(cls, data):
        return cls(**data)
