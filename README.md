# 🚀 SkillSphere – Skill-Based Job Recommendation System

## 📌 Overview

SkillSphere is a Python-based job recommendation system that matches user skills and location with relevant job listings.  
The system analyzes skill overlap, calculates match percentage, and suggests suitable job opportunities along with skill gap insights.

This project simulates real-world job discovery logic using core Python concepts and structured data handling.

---

## ⚙️ Technologies Used

- Python
- JSON (for job database storage)
- Core Data Structures (Lists, Dictionaries, Sets)

---

## ✨ Features

- 🔍 Skill-based job matching using set intersection logic
- 📍 Location-based filtering for nearby opportunities
- 📊 Match percentage calculation for ranking jobs
- 🧠 Skill gap analysis to suggest missing skills
- 📂 External JSON-based job database

---

## 🗂️ Project Structure

```
Skillsphere/
│
├── jobs_database.json   # Job listings database
├── main.py              # Main application logic
└── README.md
```

---

## ▶️ How to Run the Project

1. Clone the repository or download the files.
2. Make sure Python is installed on your system.
3. Run the following command:

```
python main.py
```

4. Enter your city and skills when prompted.
5. The system will display ranked job recommendations.

---

## 🧠 How It Works

- User inputs skills and location.
- The system compares user skills with job requirements using set intersection.
- A match percentage is calculated.
- Additional score is added for location match.
- Jobs are ranked and displayed in descending order.
- Missing skills are shown to help users understand learning gaps.

---

## 🔮 Future Enhancements

- Convert CLI application into a Web Application (Flask/Streamlit)
- Integrate real-time job APIs
- Add experience-based filtering
- Implement database integration (MySQL/PostgreSQL)
- Deploy as a cloud-based service

---

## 👨‍💻 Author

Developer : Sarthak Tiwary
