
# AskAway

AskAway is a web-based question and answer platform that allows users to ask questions, provide answers, and engage with a community of curious minds. Built with Django, this platform provides a clean, intuitive interface for knowledge sharing.

---

## 🚀 Features

### 🔐 User Authentication
- Sign up with strong password validation  
- Login/logout functionality   

### ❓ Question Management
- Ask questions with titles and detailed descriptions  
- Browse questions from the community  

### 💬 Answer System
- Post answers to questions  
- View all answers for a specific question  
- Like answers
---

## ⚙️ Installation

### 📦 Prerequisites
- Python 3.8 or higher  
- pip (Python package manager)  
- Git  

### 🧪 Setup Instructions

Clone the repository:
```bash
git clone https://github.com/AMALDEEP-P/askaway.git
cd askaway
```

Create and activate a virtual environment:
```bash
python -m venv venv

# On Windows
venv\Scripts\activate

# On macOS/Linux
source venv/bin/activate
```

Install dependencies:
```bash
pip install -r requirements.txt
```

Run migrations:
```bash
python manage.py migrate
```
Create a superuser:
```bash
python manage.py createsuperuser
```

Run the development server:
```bash
python manage.py runserver
```

