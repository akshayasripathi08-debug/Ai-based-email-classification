📧 AI-Based Email Spam Classification (SpamSense)
🚀 Overview

SpamSense is a full-stack web application that classifies email/SMS messages as Spam or Ham (Not Spam) using a lightweight machine learning-inspired heuristic model.

The project features a modern dashboard-style UI and a Flask-based backend API for real-time classification.

🧠 Features
📩 Real-time spam detection
🌐 REST API using Flask
💻 Interactive frontend dashboard
⚡ Fast keyword-based classification
📊 Confidence score display
🔄 Cross-Origin support (CORS enabled)
🏗️ Project Structure
Ai-based-email-classification-main/
│
├── app.py              # Flask backend API
├── index.html          # Frontend UI
├── style.css           # Styling
├── script.js           # Frontend logic
├── requirements.txt    # Python dependencies
├── LICENSE
└── README.md
⚙️ Technologies Used
Python (Flask)
HTML, CSS, JavaScript
REST API
VS Code (recommended IDE)
🧪 How It Works

The backend analyzes input text using predefined spam keywords such as:

"win"
"free"
"money"
"urgent"

Based on keyword matches, it calculates:

Spam probability
Ham probability
Confidence score
🖥️ How to Run the Project in VS Code
🔹 Step 1: Download the Project
Clone the repository:
git clone https://github.com/your-username/your-repo-name.git

OR download ZIP and extract.

🔹 Step 2: Open in VS Code
Open VS Code
Click File → Open Folder
Select the project folder
🔹 Step 3: Create Virtual Environment (Recommended)
python -m venv venv

Activate it:

Windows:
venv\Scripts\activate
🔹 Step 4: Install Dependencies
pip install -r requirements.txt
🔹 Step 5: Run Flask Server
python app.py

You should see:

SpamSense API Running
🔹 Step 6: Open Frontend
Open index.html in your browser
OR
Use VS Code Live Server extension
🔗 API Endpoint
POST /api/classify
Request:
{
  "text": "You won free money!"
}
Response:
{
  "is_spam": true,
  "spam_probability": 80,
  "ham_probability": 20,
  "confidence": 80,
  "confidence_label": "High",
  "signals": [],
  "model_used": "Basic Model"
}
📸 Screenshots (Optional)

Add your UI screenshots here

📌 Future Improvements
Integrate ML models (Naive Bayes, SVM)
Add database for history tracking
Improve UI/UX design
Deploy on cloud (Heroku / Render)
👨‍💻 Author
Your Name
📜 License

This project is licensed under the MIT License.

⭐ Contributing

Contributions are welcome! Feel free to fork this repo and submit a pull request.

💡 Notes for Users
Ensure Python is installed (version 3.7+ recommended)
If port 10000 is busy, modify it in app.py
Use tools like Postman for API testing
