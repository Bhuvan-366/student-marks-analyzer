# Student Marks Analyzer

A simple Python project that analyzes student marks from a CSV file, generates a report, runs automated tests using Pytest, and uses GitHub Actions for Continuous Integration (CI).

---

## Features

- Read student marks from a CSV file
- Calculate average marks
- Identify the topper
- Generate a report automatically
- Unit testing with Pytest
- Automated workflow using GitHub Actions
- Upload generated report as a GitHub Actions Artifact

---

## Project Structure

```text
student-marks-analyzer/
│
├── data/
│   └── students.csv
│
├── reports/
│   └── report.txt
│
├── analyzer.py
├── test_analyzer.py
├── requirements.txt
├── .gitignore
│
└── .github/
    └── workflows/
        └── analyze.yml
```

---

## Sample Input

`data/students.csv`

```csv
Name,Marks
A,90
B,80
C,95
D,78
E,88
```

---

## Sample Output

`reports/report.txt`

```text
Student Marks Report
====================

Average Marks: 86.20

Topper:
C - 95

Total Students:
5
```

---

## Installation

### Clone Repository

```bash
git clone https://github.com/<your-username>/student-marks-analyzer.git
cd student-marks-analyzer
```

### Create Virtual Environment

```bash
python -m venv .venv
```

### Activate Virtual Environment

Windows:

```bash
.venv\Scripts\activate
```

Linux / Mac:

```bash
source .venv/bin/activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

---

## Run the Analyzer

```bash
python analyzer.py
```

Generated report:

```text
reports/report.txt
```

---

## Run Tests

```bash
pytest
```

Expected Output:

```text
2 passed
```

---

## GitHub Actions Workflow

The workflow automatically executes whenever code is pushed to the repository.

Workflow Steps:

1. Checkout repository
2. Setup Python
3. Install dependencies
4. Run Pytest tests
5. Generate report
6. Upload report as Artifact

Workflow file:

```text
.github/workflows/analyze.yml
```

---

## Download Generated Report

After a successful workflow run:

1. Open the repository
2. Go to **Actions**
3. Select the latest workflow run
4. Download the **student-report** artifact

---

## Technologies Used

- Python 3.13
- CSV Module
- Pytest
- Git
- GitHub
- GitHub Actions

---

## Learning Outcomes

This project demonstrates:

- File Handling in Python
- CSV Processing
- Unit Testing
- Virtual Environments
- Git & GitHub
- Continuous Integration (CI)
- GitHub Actions Workflows
- Artifact Management

---

## Future Improvements

- Subject-wise analysis
- Leaderboard generation
- Graphical reports
- PDF report generation
- Automatic report commit to repository
- Email notifications for report generation

---

## Author

Bhuvan
