"""
Preset College Information Data (Departments, Curricula, Fee Structures, Senior Reviews)
"""

DEPARTMENTS = {
    "1": {
        "code": "CSE",
        "name": "Computer Science & Engineering",
        "description": "Focuses on software engineering, data structures, algorithms, cloud computing, and web development.",
        "head_of_dept": "Dr. A. K. Sharma",
        "seats_btech": 180,
        "seats_mtech": 30
    },
    "2": {
        "code": "AIML",
        "name": "Artificial Intelligence & Machine Learning",
        "description": "Specialized degree in machine learning algorithms, deep learning, computer vision, and NLP.",
        "head_of_dept": "Dr. Radhika Sen",
        "seats_btech": 120,
        "seats_mtech": 24
    },
    "3": {
        "code": "ECE",
        "name": "Electronics & Communication Engineering",
        "description": "Covers embedded systems, VLSI design, signal processing, IoT, and telecommunications.",
        "head_of_dept": "Dr. V. Prasad",
        "seats_btech": 120,
        "seats_mtech": 18
    },
    "4": {
        "code": "IT",
        "name": "Information Technology",
        "description": "Prepares students for IT systems administration, cybersecurity, database architecture, and DevOps.",
        "head_of_dept": "Dr. S. Mukherjee",
        "seats_btech": 120,
        "seats_mtech": 18
    },
    "5": {
        "code": "ME",
        "name": "Mechanical Engineering",
        "description": "Emphasizes thermal engineering, robotics, CAD/CAM design, and industrial automation.",
        "head_of_dept": "Dr. R. C. Verma",
        "seats_btech": 60,
        "seats_mtech": 12
    }
}

COURSE_STRUCTURES = {
    "B.Tech": {
        "CSE": {
            "Sem 1": [("CS101", "Programming in Python", 4), ("MA101", "Calculus & Linear Algebra", 4), ("PH101", "Engineering Physics", 3)],
            "Sem 2": [("CS102", "Data Structures & Algorithms", 4), ("CS103", "Digital Logic Design", 3), ("EE101", "Basic Electrical Engg", 3)],
            "Sem 3": [("CS201", "Object Oriented Programming (Java/Python)", 4), ("CS202", "Database Management Systems", 4), ("CS203", "Operating Systems", 3)],
            "Sem 4": [("CS204", "Computer Networks", 4), ("CS205", "Software Engineering", 3), ("CS206", "Web Technologies", 3)]
        },
        "AIML": {
            "Sem 1": [("AI101", "Python for Data Science", 4), ("MA101", "Calculus & Linear Algebra", 4), ("PH101", "Engineering Physics", 3)],
            "Sem 2": [("AI102", "Data Structures with Python", 4), ("MA102", "Probability & Statistics", 4), ("AI103", "Intro to Artificial Intelligence", 3)],
            "Sem 3": [("AI201", "Machine Learning Foundations", 4), ("AI202", "Data Mining & Visualization", 3), ("CS202", "Database Management Systems", 4)],
            "Sem 4": [("AI203", "Deep Learning & Neural Networks", 4), ("AI204", "Natural Language Processing", 3), ("AI205", "Computer Vision", 3)]
        },
        "ECE": {
            "Sem 1": [("EC101", "Circuit Theory & Networks", 4), ("MA101", "Calculus & Linear Algebra", 4), ("PH101", "Engineering Physics", 3)],
            "Sem 2": [("EC102", "Electronic Devices & Circuits", 4), ("EC103", "Digital Electronics", 3), ("CS101", "Programming in Python", 4)],
            "Sem 3": [("EC201", "Signals & Systems", 4), ("EC202", "Analog Communications", 4), ("EC203", "Electromagnetic Theory", 3)],
            "Sem 4": [("EC204", "Microprocessors & Microcontrollers", 4), ("EC205", "VLSI Design Fundamentals", 3), ("EC206", "Embedded Systems", 3)]
        },
        "IT": {
            "Sem 1": [("IT101", "Problem Solving using Python", 4), ("MA101", "Calculus & Linear Algebra", 4), ("PH101", "Engineering Physics", 3)],
            "Sem 2": [("IT102", "Data Structures & Applications", 4), ("IT103", "Computer Organization", 3), ("IT104", "Discrete Mathematics", 3)],
            "Sem 3": [("IT201", "Database Systems & SQL", 4), ("IT202", "Object Oriented System Design", 3), ("IT203", "Cyber Security Basics", 3)],
            "Sem 4": [("IT204", "Cloud Computing & DevOps", 4), ("IT205", "Web Development Frameworks", 4), ("IT206", "Network Security", 3)]
        },
        "ME": {
            "Sem 1": [("ME101", "Engineering Mechanics", 4), ("MA101", "Calculus & Linear Algebra", 4), ("PH101", "Engineering Physics", 3)],
            "Sem 2": [("ME102", "Thermodynamics", 4), ("ME103", "Engineering Graphics & CAD", 3), ("ME104", "Material Science", 3)],
            "Sem 3": [("ME201", "Fluid Mechanics & Machinery", 4), ("ME202", "Manufacturing Technology", 4), ("ME203", "Strength of Materials", 3)],
            "Sem 4": [("ME204", "Kinematics of Machinery", 4), ("ME205", "Heat & Mass Transfer", 3), ("ME206", "Industrial Robotics", 3)]
        }
    },
    "M.Tech": {
        "CSE": {
            "Sem 1": [("CS501", "Advanced Data Structures & Algorithms", 4), ("CS502", "Distributed Systems Architecture", 4)],
            "Sem 2": [("CS503", "Advanced Cloud Architecture", 4), ("CS504", "High Performance Computing", 4)],
            "Sem 3": [("CS601", "Dissertation Phase-I / Research", 8)],
            "Sem 4": [("CS602", "Dissertation Phase-II / Defense", 12)]
        },
        "AIML": {
            "Sem 1": [("AI501", "Advanced Machine Learning Theory", 4), ("AI502", "Deep Learning Architecture & Optimization", 4)],
            "Sem 2": [("AI503", "Reinforcement Learning & Autonomous Agents", 4), ("AI504", "Generative AI & LLM Systems", 4)],
            "Sem 3": [("AI601", "AI Research Thesis Phase-I", 8)],
            "Sem 4": [("AI602", "AI Research Thesis Phase-II", 12)]
        },
        "ECE": {
            "Sem 1": [("EC501", "Advanced Embedded & Real-Time Systems", 4), ("EC502", "Nano-Electronics & VLSI", 4)],
            "Sem 2": [("EC503", "Wireless Communication Networks", 4), ("EC504", "Digital Signal Processors", 4)],
            "Sem 3": [("EC601", "PG Project Phase-I", 8)],
            "Sem 4": [("EC602", "PG Project Phase-II", 12)]
        }
    }
}

FEE_STRUCTURE = {
    "B.Tech": {
        "Tuition Fee (Per Year)": 115000,
        "Admission & Registration Fee (One-time)": 15000,
        "Library & Lab Security Deposit (Refundable)": 10000,
        "Examination Fee (Per Year)": 6000,
        "Hostel & Mess Fee (Optional / Per Year)": 75000,
        "Bus Transportation (Optional / Per Year)": 25000
    },
    "M.Tech": {
        "Tuition Fee (Per Year)": 95000,
        "Admission & Registration Fee (One-time)": 12000,
        "Library & Lab Security Deposit (Refundable)": 10000,
        "Examination Fee (Per Year)": 6000,
        "Hostel & Mess Fee (Optional / Per Year)": 75000,
        "Bus Transportation (Optional / Per Year)": 25000
    }
}

SCHOLARSHIPS = [
    {"name": "Merit Excellence Scholarship", "criteria": "90%+ in 10+2 / B.Tech", "discount_pct": 30},
    {"name": "Academic Distinction Scholarship", "criteria": "80% to 89.9% in 10+2 / B.Tech", "discount_pct": 15},
    {"name": "Women in Tech Scholarship", "criteria": "Female engineering aspirants", "discount_pct": 10},
    {"name": "Sports / National Talent Award", "criteria": "State/National level sports representation", "discount_pct": 20}
]

DEFAULT_SENIOR_REVIEWS = [
    {
        "reviewer_name": "Rohan Deshmukh",
        "degree": "B.Tech",
        "department": "CSE",
        "passout_year": 2025,
        "rating": 5,
        "review_text": "Awesome campus life! The Python & AI labs are top notch. Got placed at Amazon with 24 LPA. Focus on Data Structures from 1st year.",
        "company_placed": "Amazon (24 LPA)"
    },
    {
        "reviewer_name": "Ananya Kulkarni",
        "degree": "B.Tech",
        "department": "AIML",
        "passout_year": 2024,
        "rating": 5,
        "review_text": "The faculty in AI/ML is super helpful. We worked on real-world computer vision projects. Placed at Microsoft!",
        "company_placed": "Microsoft (28 LPA)"
    },
    {
        "reviewer_name": "Vikram Singh",
        "degree": "B.Tech",
        "department": "ECE",
        "passout_year": 2024,
        "rating": 4,
        "review_text": "Great VLSI & Robotics labs. Faculty guides you for GATE exam as well as campus placements. Good infrastructure.",
        "company_placed": "Qualcomm (16 LPA)"
    },
    {
        "reviewer_name": "Priya Nair",
        "degree": "M.Tech",
        "department": "CSE",
        "passout_year": 2025,
        "rating": 5,
        "review_text": "M.Tech program offers deep research exposure. Flexible timings for lab work and stipend assistance available.",
        "company_placed": "TCS Research (14 LPA)"
    }
]
