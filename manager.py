"""
College System Manager (Data Controller & Business Logic using Core Python Concepts)
"""

import os
import json
from models import Student, Faculty, Course, SeniorReview
from college_data import DEPARTMENTS, COURSE_STRUCTURES, FEE_STRUCTURE, SCHOLARSHIPS, DEFAULT_SENIOR_REVIEWS

DATA_DIR = os.path.join(os.path.dirname(__file__), 'data')
DATA_FILE = os.path.join(DATA_DIR, 'college_system.json')

class CollegeSystemManager:
    def __init__(self):
        self.students = {}
        self.faculty = {}
        self.senior_reviews = []
        self.ensure_data_dir()
        self.load_data()

    def ensure_data_dir(self):
        if not os.path.exists(DATA_DIR):
            os.makedirs(DATA_DIR, exist_ok=True)

    def load_data(self):
        """Load JSON data from file or seed default data"""
        if os.path.exists(DATA_FILE):
            try:
                with open(DATA_FILE, 'r', encoding='utf-8') as f:
                    content = json.load(f)
                    
                # Load students
                for s_data in content.get("students", []):
                    st = Student.from_dict(s_data)
                    self.students[st.person_id] = st
                    
                # Load faculty
                for f_data in content.get("faculty", []):
                    fac = Faculty.from_dict(f_data)
                    self.faculty[fac.person_id] = fac
                    
                # Load senior reviews
                for r_data in content.get("senior_reviews", []):
                    rev = SeniorReview.from_dict(r_data)
                    self.senior_reviews.append(rev)
            except Exception as e:
                print(f"[Warning] Error loading data file: {e}. Seeding initial data...")
                self.seed_default_data()
        else:
            self.seed_default_data()

    def save_data(self):
        """Save data to JSON file (File I/O)"""
        data = {
            "students": [st.to_dict() for st in self.students.values()],
            "faculty": [fac.to_dict() for fac in self.faculty.values()],
            "senior_reviews": [rev.to_dict() for rev in self.senior_reviews]
        }
        with open(DATA_FILE, 'w', encoding='utf-8') as f:
            json.dump(data, f, indent=4)

    def seed_default_data(self):
        """Seed default faculty & senior reviews"""
        self.senior_reviews = [SeniorReview.from_dict(r) for r in DEFAULT_SENIOR_REVIEWS]

        # Sample Faculty Members
        sample_faculty = [
            Faculty("FAC101", "Dr. A. K. Sharma", "aksharma@college.edu", "9876543210", "Male", "CSE", "Professor & HOD", 140000),
            Faculty("FAC102", "Dr. Radhika Sen", "radhika.sen@college.edu", "9876543211", "Female", "AIML", "Professor & HOD", 145000),
            Faculty("FAC103", "Prof. Suresh Kumar", "suresh.k@college.edu", "9876543212", "Male", "ECE", "Assoc. Professor", 95000),
            Faculty("FAC104", "Dr. S. Mukherjee", "smukherjee@college.edu", "9876543213", "Male", "IT", "Professor & HOD", 135000),
        ]
        for fac in sample_faculty:
            self.faculty[fac.person_id] = fac

        # Sample Registered Students
        sample_students = [
            Student("STU202501", "Aarav Sharma", "aarav@gmail.com", "9123456780", "Male", "B.Tech", "CSE", 1, 115000.0),
            Student("STU202502", "Sneha Patel", "sneha@gmail.com", "9123456781", "Female", "B.Tech", "AIML", 1, 125000.0),
            Student("STU202503", "Rahul Verma", "rahul@gmail.com", "9123456782", "Male", "M.Tech", "CSE", 1, 95000.0)
        ]
        for st in sample_students:
            self.students[st.person_id] = st

        self.save_data()

    # --- Admission Guidance Operations ---
    def generate_student_id(self, degree):
        prefix = "STU-B" if degree == "B.Tech" else "STU-M"
        count = len(self.students) + 101
        return f"{prefix}{count}"

    def register_new_admission(self, name, email, phone, gender, degree, dept_code, need_hostel=False, need_bus=False, scholarship_idx=None):
        """Registers a new student during admission guidance"""
        student_id = self.generate_student_id(degree)

        # Fee Calculation
        base_tuition = FEE_STRUCTURE[degree]["Tuition Fee (Per Year)"]
        admission_fee = FEE_STRUCTURE[degree]["Admission & Registration Fee (One-time)"]
        security_dep = FEE_STRUCTURE[degree]["Library & Lab Security Deposit (Refundable)"]
        exam_fee = FEE_STRUCTURE[degree]["Examination Fee (Per Year)"]
        
        hostel_fee = FEE_STRUCTURE[degree]["Hostel & Mess Fee (Optional / Per Year)"] if need_hostel else 0
        bus_fee = FEE_STRUCTURE[degree]["Bus Transportation (Optional / Per Year)"] if need_bus else 0

        subtotal = base_tuition + admission_fee + security_dep + exam_fee + hostel_fee + bus_fee

        discount_pct = 0
        scholarship_name = "None"
        if scholarship_idx is not None and 0 <= scholarship_idx < len(SCHOLARSHIPS):
            sch = SCHOLARSHIPS[scholarship_idx]
            discount_pct = sch["discount_pct"]
            scholarship_name = sch["name"]

        discount_amount = (base_tuition * discount_pct) / 100.0
        final_total_fee = subtotal - discount_amount

        student = Student(
            person_id=student_id,
            name=name,
            email=email,
            phone=phone,
            gender=gender,
            degree=degree,
            department=dept_code,
            year=1,
            fee_paid=final_total_fee
        )

        self.students[student_id] = student
        self.save_data()

        fee_receipt = {
            "Student ID": student_id,
            "Name": name,
            "Degree": degree,
            "Department": dept_code,
            "Base Tuition": base_tuition,
            "Admission Fee": admission_fee,
            "Security Deposit": security_dep,
            "Exam Fee": exam_fee,
            "Hostel Fee": hostel_fee,
            "Bus Fee": bus_fee,
            "Scholarship": scholarship_name,
            "Discount Amount": discount_amount,
            "Final Total Payable": final_total_fee
        }

        return student, fee_receipt

    # --- Student Portal Operations ---
    def get_all_students(self):
        return list(self.students.values())

    def search_student(self, query):
        query = query.lower()
        return [
            s for s in self.students.values()
            if query in s.person_id.lower() or query in s.name.lower() or query in s.department.lower()
        ]

    def remove_student(self, student_id):
        if student_id in self.students:
            del self.students[student_id]
            self.save_data()
            return True
        return False

    # --- Faculty Operations ---
    def get_all_faculty(self):
        return list(self.faculty.values())

    def add_faculty(self, name, email, phone, gender, department, designation, salary):
        fac_id = f"FAC{len(self.faculty) + 105}"
        faculty = Faculty(fac_id, name, email, phone, gender, department, designation, salary)
        self.faculty[fac_id] = faculty
        self.save_data()
        return faculty

    # --- Senior Reviews Operations ---
    def add_senior_review(self, reviewer_name, degree, department, passout_year, rating, review_text, company_placed):
        rev = SeniorReview(reviewer_name, degree, department, passout_year, rating, review_text, company_placed)
        self.senior_reviews.append(rev)
        self.save_data()
        return rev

    def get_senior_reviews(self, dept_code=None):
        if dept_code:
            return [r for r in self.senior_reviews if r.department == dept_code]
        return self.senior_reviews
