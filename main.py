"""
College Management & Student Admission Guidance System - Main Interactive CLI Entry Point
Developed entirely in Core Python (OOP, File I/O, Data Structures, Exception Handling)
"""

import sys
from manager import CollegeSystemManager
from college_data import DEPARTMENTS, COURSE_STRUCTURES, FEE_STRUCTURE, SCHOLARSHIPS
from cli_utils import (
    print_banner, print_section, print_table,
    get_menu_choice, prompt_input, prompt_number
)

def run_admission_helpdesk(manager):
    """Guided Admission Workflow: Welcome -> Degree -> Specialization -> Course Structure -> Fee Structure -> Senior Reviews -> Application"""
    print_banner("🎓 WELCOME TO APEX COLLEGE OF ENGINEERING & TECHNOLOGY", "Guided Admission & Academic Discovery Portal")
    
    applicant_name = prompt_input("Enter Prospective Student's Name")
    applicant_email = prompt_input("Enter Contact Email")
    applicant_phone = prompt_input("Enter Phone Number")
    gender = get_menu_choice({"1": "Male", "2": "Female", "3": "Other"}, "Select Gender")
    gender_str = "Male" if gender == "1" else ("Female" if gender == "2" else "Other")

    print(f"\nWelcome, {applicant_name}! Let's guide you step-by-step through your academic journey.\n")

    # Step 1: Degree Selection (B.Tech vs M.Tech)
    print_section("Step 1: Choose Academic Program (Degree)")
    deg_choice = get_menu_choice({
        "1": "B.Tech (Bachelor of Technology - 4 Years / 8 Semesters)",
        "2": "M.Tech (Master of Technology - 2 Years / 4 Semesters)"
    }, "Select Degree Program")
    
    degree = "B.Tech" if deg_choice == "1" else "M.Tech"
    print(f"\n✔ Selected Program: {degree}")

    # Step 2: Department & Specialization Selector
    print_section("Step 2: Explore Departments & Specializations")
    print("Available Engineering Departments:")
    for key, dept in DEPARTMENTS.items():
        seats = dept["seats_btech"] if degree == "B.Tech" else dept["seats_mtech"]
        print(f"  [{key}] {dept['code']} - {dept['name']} (HOD: {dept['head_of_dept']} | Seats: {seats})")
        print(f"      Description: {dept['description']}")
    
    dept_choice = get_menu_choice({
        "1": "Computer Science & Engineering (CSE)",
        "2": "Artificial Intelligence & Machine Learning (AIML)",
        "3": "Electronics & Communication Engineering (ECE)",
        "4": "Information Technology (IT)",
        "5": "Mechanical Engineering (ME)"
    }, "Select Department / Specialization")

    dept_info = DEPARTMENTS[dept_choice]
    dept_code = dept_info["code"]
    print(f"\n✔ Selected Specialization: {dept_info['name']} ({dept_code})")

    # Step 3: Course Structure & Semester Curriculum Explorer
    print_section("Step 3: Course Structure & Semester Curriculum")
    print(f"Curriculum Breakdown for {degree} in {dept_code}:")

    curriculum = COURSE_STRUCTURES.get(degree, {}).get(dept_code, {})
    if curriculum:
        for sem, courses in curriculum.items():
            print(f"\n  📘 {sem}:")
            headers = ["Course Code", "Subject Name", "Credits"]
            rows = [[c[0], c[1], c[2]] for c in courses]
            print_table(headers, rows)
    else:
        print("  Curriculum details available at campus academic desk.")

    # Step 4: Fee Structure & Scholarship Calculator
    print_section("Step 4: Fee Structure & Annual Costs")
    print(f"Annual Fee Breakdown for {degree}:")
    
    fee_headers = ["Fee Component", "Amount (₹)"]
    fee_rows = [[comp, f"₹{amt:,.2f}"] for comp, amt in FEE_STRUCTURE[degree].items()]
    print_table(fee_headers, fee_rows)

    print("\nOptional Services Selection:")
    need_hostel_choice = get_menu_choice({"1": "Yes (₹75,000/yr)", "2": "No"}, "Require Campus Hostel & Mess Facility?")
    need_bus_choice = get_menu_choice({"1": "Yes (₹25,000/yr)", "2": "No"}, "Require Bus Transportation?")
    
    need_hostel = (need_hostel_choice == "1")
    need_bus = (need_bus_choice == "1")

    print("\nAvailable Merit & Category Scholarships:")
    for idx, sch in enumerate(SCHOLARSHIPS):
        print(f"  [{idx+1}] {sch['name']} ({sch['discount_pct']}% Tuition Discount) - Criteria: {sch['criteria']}")
    print("  [0] None / Not Applicable")

    sch_choice = prompt_number("Select Scholarship Option (0-4)", int, 0, len(SCHOLARSHIPS))
    sch_idx = (sch_choice - 1) if sch_choice > 0 else None

    # Step 5: Senior Student Reviews & Testimonials
    print_section("Step 5: Senior Student Reviews & Campus Placement Insights")
    print(f"What Seniors say about {dept_code} & Apex College:")

    reviews = manager.get_senior_reviews(dept_code)
    if not reviews:
        reviews = manager.get_senior_reviews() # Fallback to all reviews

    for r in reviews:
        stars = "★" * r.rating + "☆" * (5 - r.rating)
        print(f"\n  💬 {r.reviewer_name} ({r.degree} {r.department}, Batch {r.passout_year}) - Rating: {stars}")
        print(f"     Placed at: {r.company_placed}")
        print(f"     Review: \"{r.review_text}\"")

    # Step 6: Final Admission Confirmation & Application Receipt
    print_section("Step 6: Submit Admission Application & Generate Fee Receipt")
    confirm_choice = get_menu_choice({"1": "Yes, Submit Application", "2": "Cancel & Return to Menu"}, "Confirm Application Submission?")

    if confirm_choice == "1":
        student, receipt = manager.register_new_admission(
            name=applicant_name,
            email=applicant_email,
            phone=applicant_phone,
            gender=gender_str,
            degree=degree,
            dept_code=dept_code,
            need_hostel=need_hostel,
            need_bus=need_bus,
            scholarship_idx=sch_idx
        )

        print_banner("🎉 ADMISSION SUCCESSFUL & CONFIRMED!", f"Student ID Assigned: {student.person_id}")
        
        print("Official Admission Fee Receipt:")
        receipt_rows = [[k, f"₹{v:,.2f}" if isinstance(v, (int, float)) and "ID" not in k else str(v)] for k, v in receipt.items()]
        print_table(["Field / Component", "Details"], receipt_rows)

        print("\nThank you for choosing Apex College of Engineering & Technology!")
        print("Our academic desk will contact you via email for original document verification.\n")
    else:
        print("\nAdmission application cancelled. Returning to main menu...")


def run_management_portal(manager):
    """Admin & Management Operations Portal"""
    while True:
        print_section("College Administration & Management Portal")
        options = {
            "1": "View All Registered Students",
            "2": "Search Student by Name / ID / Dept",
            "3": "Remove Student Record",
            "4": "View Faculty Directory",
            "5": "Add New Faculty Member",
            "6": "Add Senior Student Review / Placement Record",
            "7": "View All Senior Reviews",
            "8": "Return to Main Menu"
        }
        choice = get_menu_choice(options, "Select Administrative Task")

        if choice == "1":
            students = manager.get_all_students()
            print_section("Registered Students List")
            headers = ["Student ID", "Name", "Degree", "Department", "Year", "Fee Total"]
            rows = [[s.person_id, s.name, s.degree, s.department, f"Year {s.year}", f"₹{s.fee_paid:,.2f}"] for s in students]
            print_table(headers, rows)

        elif choice == "2":
            query = prompt_input("Enter Student ID, Name, or Department to Search")
            results = manager.search_student(query)
            print_section(f"Search Results for '{query}' ({len(results)} found)")
            headers = ["Student ID", "Name", "Degree", "Department", "Email", "Phone"]
            rows = [[s.person_id, s.name, s.degree, s.department, s.email, s.phone] for s in results]
            print_table(headers, rows)

        elif choice == "3":
            st_id = prompt_input("Enter Student ID to Remove")
            if manager.remove_student(st_id):
                print(f"✔ Student '{st_id}' successfully removed from college records.")
            else:
                print(f"❌ Student ID '{st_id}' not found.")

        elif choice == "4":
            faculty_members = manager.get_all_faculty()
            print_section("Faculty Members Directory")
            headers = ["Faculty ID", "Name", "Department", "Designation", "Email", "Phone"]
            rows = [[f.person_id, f.name, f.department, f.designation, f.email, f.phone] for f in faculty_members]
            print_table(headers, rows)

        elif choice == "5":
            print_section("Add New Faculty Member")
            name = prompt_input("Faculty Name")
            email = prompt_input("Email")
            phone = prompt_input("Phone Number")
            gender = get_menu_choice({"1": "Male", "2": "Female", "3": "Other"}, "Select Gender")
            gender_str = "Male" if gender == "1" else ("Female" if gender == "2" else "Other")
            dept = prompt_input("Department (CSE/AIML/ECE/IT/ME)")
            designation = prompt_input("Designation (e.g. Asst. Professor)")
            salary = prompt_number("Monthly Salary (₹)", float, min_val=20000)

            fac = manager.add_faculty(name, email, phone, gender_str, dept, designation, salary)
            print(f"✔ Faculty member '{fac.name}' added with ID: {fac.person_id}")

        elif choice == "6":
            print_section("Add Senior Review / Placement Feedback")
            name = prompt_input("Reviewer Senior Name")
            degree = get_menu_choice({"1": "B.Tech", "2": "M.Tech"}, "Degree")
            degree_str = "B.Tech" if degree == "1" else "M.Tech"
            dept = prompt_input("Department Code (CSE/AIML/ECE/IT/ME)")
            year = prompt_number("Passout Year", int, min_val=2015, max_val=2026)
            rating = prompt_number("Rating Star (1 to 5)", int, min_val=1, max_val=5)
            company = prompt_input("Company Placed & Package (e.g. Google - 22 LPA)")
            review_text = prompt_input("Senior Advice / Review Comment")

            manager.add_senior_review(name, degree_str, dept, year, rating, review_text, company)
            print(f"✔ Senior review for {name} saved successfully.")

        elif choice == "7":
            print_section("All Senior Student Reviews & Campus Testimonials")
            reviews = manager.get_senior_reviews()
            for r in reviews:
                stars = "★" * r.rating + "☆" * (5 - r.rating)
                print(f"  💬 {r.reviewer_name} ({r.degree} {r.department}, {r.passout_year}) | Rating: {stars}")
                print(f"     Placed at: {r.company_placed}")
                print(f"     Review: \"{r.review_text}\"\n")

        elif choice == "8":
            break


def main():
    manager = CollegeSystemManager()

    while True:
        print_banner("🏛️ COLLEGE MANAGEMENT & ADMISSION GUIDANCE SYSTEM", "Developed with Core Python Concepts (OOP, File I/O, Structures)")
        
        main_menu = {
            "1": "Prospective Student Admission Guidance (Step-by-Step Portal)",
            "2": "College Administration & Student Records Portal",
            "3": "Browse Senior Student Reviews & Campus Testimonials",
            "4": "View Course Structures & Curricula by Department",
            "5": "Exit Program"
        }

        choice = get_menu_choice(main_menu, "Select Main Portal Option")

        if choice == "1":
            run_admission_helpdesk(manager)

        elif choice == "2":
            run_management_portal(manager)

        elif choice == "3":
            print_section("Senior Student Reviews & Campus Feedback")
            reviews = manager.get_senior_reviews()
            for r in reviews:
                stars = "★" * r.rating + "☆" * (5 - r.rating)
                print(f"  💬 {r.reviewer_name} ({r.degree} {r.department}, {r.passout_year}) | Rating: {stars}")
                print(f"     Placed at: {r.company_placed}")
                print(f"     Review: \"{r.review_text}\"\n")

        elif choice == "4":
            print_section("Course Structure & Department Curricula")
            degree_choice = get_menu_choice({"1": "B.Tech", "2": "M.Tech"}, "Select Degree")
            deg = "B.Tech" if degree_choice == "1" else "M.Tech"
            dept_code = prompt_input("Enter Department Code (CSE / AIML / ECE / IT / ME)").upper()
            
            curriculum = COURSE_STRUCTURES.get(deg, {}).get(dept_code, {})
            if curriculum:
                print(f"\n📘 {deg} - {dept_code} Semester Curriculum:")
                for sem, courses in curriculum.items():
                    print(f"\n  Semester: {sem}")
                    headers = ["Code", "Subject Name", "Credits"]
                    rows = [[c[0], c[1], c[2]] for c in courses]
                    print_table(headers, rows)
            else:
                print(f"❌ Curriculum not found for {deg} {dept_code}.")

        elif choice == "5":
            print_banner("THANK YOU FOR VISITING APEX COLLEGE OF ENGINEERING!", "We wish you all the best for your academic journey.")
            sys.exit(0)


if __name__ == '__main__':
    main()
