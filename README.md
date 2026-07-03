# Student Database Management System 🎓

A full-stack web application built with **Python (Flask)** and **MySQL** that enables complete management of student records through a clean, responsive interface. The system supports full CRUD operations with a well-structured relational database schema.

---

## ✨ Features

- ➕ **Add** new student records
- 📋 **View** all students in a structured table
- ✏️ **Update** existing student information
- 🗑️ **Delete** student records
- 🔍 **Search** students by name, roll number, or course
- 📊 Organized display with a clean, responsive UI

---

## 🛠️ Tech Stack

| Layer | Technology |
|-------|-----------|
| **Backend** | Python, Flask |
| **Database** | MySQL |
| **Frontend** | HTML, Bootstrap |
| **ORM/DB** | Flask-MySQLdb / MySQL Connector |

---

## 📁 Project Structure

```
Student-Database-Management-System/
│
├── student_dbms_project/
│   ├── app.py              # Flask application and route definitions
│   ├── templates/          # HTML templates
│   │   ├── index.html      # Home / student list view
│   │   ├── add.html        # Add student form
│   │   ├── edit.html       # Edit student form
│   │   └── ...
│   └── static/             # CSS and static assets
│
└── README.md
```

> **Note:** Update this structure to match your actual file organization.

---

## 🗄️ Database Schema

```sql
CREATE TABLE students (
    id          INT AUTO_INCREMENT PRIMARY KEY,
    name        VARCHAR(100) NOT NULL,
    roll_no     VARCHAR(20) UNIQUE NOT NULL,
    course      VARCHAR(100),
    email       VARCHAR(100),
    phone       VARCHAR(15),
    created_at  TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
```

> Update this schema to match your actual database structure.

---

## 🚀 Getting Started

### Prerequisites

- Python 3.x
- MySQL Server
- pip

### Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/kinjal-7166/Student-Database-Management-System.git
   cd Student-Database-Management-System/student_dbms_project
   ```

2. **Install dependencies**
   ```bash
   pip install flask flask-mysqldb
   ```

3. **Set up the database**
   - Open MySQL and create a database:
     ```sql
     CREATE DATABASE student_db;
     ```
   - Import the schema or run the SQL setup script
  

4. **Run the application**
   ```bash
   python app.py
   ```

5. **Open in browser**
   ```
   http://localhost:5000
   ```

---

## 📸 Key Concepts Demonstrated

- **Flask Routing** — GET and POST routes for each CRUD operation
- **MySQL Integration** — Parameterized queries to prevent SQL injection
- **Relational Database Design** — Normalized schema with primary keys and constraints
- **Template Rendering** — Dynamic HTML pages using Jinja2 templating
- **Form Handling** — Data collection and validation from HTML forms

---

## 🙋‍♀️ About

This project was built as a **personal project** to strengthen hands-on skills in full-stack web development using Python, Flask, and MySQL — focusing on real-world database design and CRUD application development.

---

## 📄 License

This project is open source and available under the [MIT License](LICENSE).

---

> ⭐ If you found this project helpful, consider giving it a star!
