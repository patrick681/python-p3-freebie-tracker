# 🧾 Freebie Tracker

A Flask-based web application that manages **Companies**, **Developers (Devs)**, and **Freebies** given by companies to devs.

---

## 📋 Overview

Freebie Tracker enables:

- Creating, reading, updating, and deleting:
  - Companies
  - Developers
  - Freebies
- Viewing all freebies owned by a developer
- Tracking which dev received what freebie from which company

---

## 🚀 Features

✅ Add, update, view, and delete companies  
✅ Add, update, view, and delete developers  
✅ Add, update, view, and delete freebies  
✅ See all freebies owned by a developer  

---

## 🛠️ How to Run the Code

### ✅ Prerequisites

- Python 3.8+
- Virtual environment (recommended)
- SQLite (default, no config needed)

### ⚙️ Setup Instructions

1. **Clone the repository**

```bash
git clone <your-repo-url>
cd python-p3-freebie-tracker
```

2. **Create and activate a virtual environment**

```bash
python3 -m venv .venv
source .venv/bin/activate       # On Windows: .venv\Scripts\activate
```

3. **Install dependencies**

```bash
pip install -r requirements.txt
```
bonus: ensure you have the selected python interpreter within the venv:
  press ctrl+shit+p
  select the interpreter found in the venv dir (ven/...)

4. **Initialize the database**

```bash
export FLASK_APP=lib.app:create_app   # On Windows: set FLASK_APP=lib.app:create_app
flask db init
flask db migrate
flask db upgrade
```

5. **Seed the database with initial data**

```bash
PYTHONPATH=. python3 lib/seed.py
```

6. **Run the development server**

```bash
PYTHONPATH=. flask run
```

💡 **Important:** Set the `PYTHONPATH` to `.` (project root) so that relative imports work.

- On **Windows Command Prompt**:
  ```cmd
  set PYTHONPATH=.
  ```

- On **Windows PowerShell**:
  ```powershell
  $env:PYTHONPATH="."
  ```

---

## 🔍 How the Code Works

| File           | Purpose                                                                 |
|----------------|-------------------------------------------------------------------------|
| `lib/app.py`   | Creates the Flask app and registers routes                              |
| `lib/models.py`| SQLAlchemy ORM models (`Company`, `Dev`, `Freebie`) and their relations |
| `lib/routes.py`| RESTful API endpoints for Companies, Devs, and Freebies                 |
| `lib/seed.py`  | Seeds the database with example data                                    |

- Uses **Flask-Migrate** for managing database migrations.
- Relationships:
  - One Company → Many Freebies
  - One Dev → Many Freebies
  - Each Freebie → One Company & One Dev

---

## 🗃️ Database Schema

```
+------------+           +-------------+            +-----------+
|  companies |           |   freebies  |            |   devs    |
+------------+           +-------------+            +-----------+
| id (PK)    |<--------+ | id (PK)      | +-------> | id (PK)   |
| name       |           | | item_name  |           | name      |
| founding_yr|           | | value      |           +-----------+
+------------+           | | company_id | (FK)       
                         | | dev_id     | (FK)      
                         +-------------+
```

### Relationships Summary

- `Company` has many `Freebies`
- `Dev` has many `Freebies`
- `Freebie` belongs to one `Company` and one `Dev`

---

## 🧪 Running Tests

We use **pytest** to run tests.

### ✅ Steps:

1. Ensure the virtual environment is activated:

```bash
source .venv/bin/activate
```

2. Run all tests:

```bash
PYTHONPATH=. pytest
```

You'll see a summary of passed and failed tests with details.

---

## 🧼 Notes

- This app uses SQLite by default.
- PostgreSQL is supported if `psycopg2-binary` is installed.
- To explore the data manually, run:

```bash
PYTHONPATH=. python3 lib/debug.py
```

---

Happy hacking! 🚀