# 🏛️ College Management & Student Admission Guidance System

[![Python](https://img.shields.io/badge/Python-3.10+-blue.svg)](https://www.python.org/)
[![Core Python](https://img.shields.io/badge/Core_Python-OOP_--_File_IO_--_CLI-emerald.svg)]()

A comprehensive, interactive menu-driven console application built **entirely using Core Python concepts**. It is specifically designed to guide prospective students step-by-step from their first welcome greeting to degree selection, department specialization, course structure exploration, fee calculation with scholarships, senior student reviews, and official admission application submission.

---

## 🎯 Core Python Concepts Demonstrated

1. **Object-Oriented Programming (OOP)**:
   - **Inheritance & Polymorphism**: `Person` base class inherited by `Student` and `Faculty` classes with overridden `get_details()` method.
   - **Encapsulation & Abstraction**: Class properties and state management encapsulated within `Course`, `SeniorReview`, and `CollegeSystemManager`.
2. **File I/O & Persistence**:
   - JSON data storage (`data/college_system.json`) ensuring student, faculty, and review records persist across program sessions.
3. **Data Structures**:
   - Nested Dictionaries, Lists, and Tuples for storing department seat matrix, fee structures, and semester curricula.
4. **Exception Handling & Validation**:
   - `try...except` blocks for graceful file loading and input validation for choices, numerical values, and phone numbers.
5. **Modular Program Structure**:
   - Decoupled into `models.py`, `college_data.py`, `manager.py`, `cli_utils.py`, and `main.py`.

---

## 🚀 Step-by-Step Guided Admission Flow

```
[1] Welcome & Student Registration
        │
        ▼
[2] Degree Selection ──► B.Tech (4 Yrs) OR M.Tech (2 Yrs)
        │
        ▼
[3] Department Specialization ──► CSE, AI & ML, ECE, IT, ME
        │
        ▼
[4] Course Structure Explorer ──► Semester-by-Semester Subjects & Credits
        │
        ▼
[5] Fee Structure & Scholarship Calculator ──► Tuition + Hostel + Transport - Discount
        │
        ▼
[6] Senior Student Reviews & Placements ──► Feedback, Ratings & Placement Packages
        │
        ▼
[7] Application Submission ──► Assigned Student ID & Official Admission Fee Receipt
```

---

## 📂 File Architecture

```
college management system/
├── main.py                # Main interactive menu & guided admission workflow
├── models.py              # OOP Classes: Person, Student, Faculty, Course, SeniorReview
├── manager.py             # CollegeSystemManager (Business logic & JSON file saving)
├── college_data.py        # Preset datasets (Departments, Curricula, Fees, Senior Reviews)
├── cli_utils.py           # Terminal formatting, banner displays, input validation
├── data/
│   └── college_system.json# JSON database file
├── README.md              # Project documentation
└── .gitignore
```

---

## ⚡ How to Run

1. Open PowerShell or Command Prompt.
2. Navigate to the project folder:
```powershell
cd "C:\Users\SASIDHAR\Desktop\college management system"
```
3. Run the application:
```powershell
python main.py
```

---

## 📋 Features Overview

- **Step-by-Step Admission Guidance**: Guides prospective students through degree choices, department seats, HOD details, and curriculum requirements.
- **Interactive Fee & Scholarship Calculator**: Computes exact payable fees based on hostel/bus options and merit scholarship percentage.
- **Senior Reviews & Placement Testimonials**: Displays real senior student reviews, star ratings, and company placement packages (e.g. Amazon 24 LPA, Microsoft 28 LPA).
- **Administration Portal**:
  - View all registered students & search by ID/Name/Department.
  - View & add faculty members with designation & salary.
  - Add senior student reviews for future applicants.
