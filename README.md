# 🎯 Difficulty Adjustment API

A simple FastAPI project that dynamically adjusts question difficulty based on user scores and previous difficulty.  
It ensures fair evaluation by preventing sudden jumps between difficulty levels and logs all transitions for tracking.

---

## 🚀 Features
- Accepts **scores (1–3 values)** and **previous difficulty** (`easy`, `medium`, `hard`).
- Returns both **previous** and **next difficulty** in JSON.
- Prevents sudden jumps (e.g., `easy → hard` becomes `easy → medium → hard`).
- Logs all requests with timestamp into `difficulty_log.json`.
- Interactive API docs via **Swagger UI**.

---

## 📂 Project Structure
```
difficulty-adjustment/
│
├── main.py              # Console script for manual input
├── logic/
│   └── difficulty.py    # Core decision logic
├── api/
│   └── server.py        # FastAPI server
├── tests/
│   └── test_logic.py    # Unit tests
└── requirements.txt     # Dependencies
```

---

## ⚙️ Installation
Clone the repo and install dependencies:
```bash
git clone https://github.com/your-username/difficulty-adjustment.git
cd difficulty-adjustment
pip install -r requirements.txt
```

---

## ▶️ Usage

### 1. Run Console Script
```bash
python main.py
```
Example:
```
Enter score 1 (or press Enter to skip): 80
Enter score 2 (or press Enter to skip): 90
Enter score 3 (or press Enter to skip): 
Enter previous difficulty (easy/medium/hard): easy

Output → {"previous_difficulty": "easy", "next_difficulty": "medium"}
```

---

### 2. Run API Server
```bash
uvicorn api.server:app --reload
```

Open in browser:
- Home → `http://127.0.0.1:8000` 
- Swagger UI → `http://127.0.0.1:8000/docs`

Example request:
```json
{
  "scores": [70, 80, 90],
  "prev_difficulty": "medium"
}
```

Example response:
```json
{
  "timestamp": "2026-06-01 20:15:00",
  "scores": [70, 80, 90],
  "previous_difficulty": "medium",
  "next_difficulty": "hard"
}
```

---

### 3. Run Tests
```bash
pytest tests/
```

---

## 📜 Log File
All runs (console + API) are appended to `difficulty_log.json`:
```json
{"timestamp": "2026-06-01 20:15:00", "scores": [70, 80, 90], "previous_difficulty": "easy", "next_difficulty": "hard"}
{"timestamp": "2026-06-01 20:16:12", "scores": [30, 40], "previous_difficulty": "medium", "next_difficulty": "medium"}
```

---

## 🛠️ Tech Stack
- **Python 3.11+**
- **FastAPI** (API framework)
- **Uvicorn** (ASGI server)
- **Pytest** (testing)

---

## 📌 Future Improvements
- Add `/logs` endpoint to view history in browser.
- Add summary stats (e.g., transitions count).
- Deploy on cloud (Heroku, Render, or Azure).

---

## 🏆 Author
👤 **Shubham Sharma**  
📍 Alwar, Rajasthan, India  
💼 2nd Year CSE Student | Python Intern

---
```

---

✅ This README is ready to commit as `README.md` in your repo. It explains your project, shows usage examples, and highlights your achievements.  

Would you like me to also add **GitHub badges** (like Python version, FastAPI, last commit, stars) at the top for extra recruiter appeal?
