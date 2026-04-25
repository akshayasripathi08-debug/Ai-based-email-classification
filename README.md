

# 📧 AI-Based Email Spam Classification System

## 🚀 Overview

This project is a **full-stack AI-powered email and SMS spam classification system** that combines **machine learning** with **real-time heuristic analysis**. It provides an interactive dashboard where users can classify messages, view history, and analyze spam detection performance.

The application is built using:

* **Frontend:** HTML, CSS, JavaScript (Single Page Application)
* **Backend:** Python Flask
* **Machine Learning:** NLP-based classification model

---

## ✨ Features

* 🔍 Real-time email/SMS spam detection
* 📊 Interactive dashboard with analytics
* 🧠 Machine Learning-based classification
* 📜 Classification history tracking
* 🌙 Dark terminal-style UI
* ⚡ Fast and responsive SPA design

---

## 🏗️ Project Structure

```
AI-based-email-classification/
│
├── static/                # CSS, JS, frontend assets
├── templates/             # HTML files
├── model/                 # Trained ML model files
├── app.py                 # Flask backend
├── requirements.txt       # Python dependencies
└── README.md              # Project documentation
```

---

## ⚙️ Requirements

Make sure you have the following installed:

* Python 3.8+
* pip (Python package manager)
* VS Code (recommended)

---

## 🧑‍💻 How to Run in VS Code

### Step 1: Extract Project

* Download or clone the repository

```bash
git clone https://github.com/your-username/AI-based-email-classification.git
```

* Open the folder in **VS Code**

---

### Step 2: Create Virtual Environment (Recommended)

```bash
python -m venv venv
```

Activate it:

**Windows:**

```bash
venv\Scripts\activate
```

**Mac/Linux:**

```bash
source venv/bin/activate
```

---

### Step 3: Install Dependencies

```bash
pip install -r requirements.txt
```

---

### Step 4: Run Flask Application

```bash
python app.py
```

---

### Step 5: Open in Browser

Go to:

```
http://127.0.0.1:5000/
```

---

## 🧪 How It Works

1. User enters email/SMS text
2. Text is processed using NLP techniques
3. Machine learning model predicts:

   * Spam ❌
   * Not Spam ✅
4. Results are displayed with probability

---

## 📊 Technologies Used

* Python (Flask)
* Machine Learning (Naive Bayes / NLP)
* HTML5, CSS3, JavaScript
* Bootstrap (optional UI styling)




## 🛠️ Troubleshooting

### ❌ Emoji Syntax Error in Python

If you see:

```
SyntaxError: invalid character '🚫'
```

👉 Fix: Replace emojis inside Python strings with plain text or use encoding:

```python
result = "SPAM"
```

---

### ❌ File Not Found Error

Make sure model files exist:

```
model/nb_model.pkl
```

---

## 📈 Future Improvements

* Add deep learning models (LSTM, BERT)
* Deploy using cloud (AWS / Heroku)
* Add user authentication
* Real-time email integration

---

## 🤝 Contribution

Contributions are welcome! Feel free to fork the repo and submit pull requests.

