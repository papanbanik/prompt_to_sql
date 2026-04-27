
#Gemini SQL Assistant (Streamlit App)

This is an AI-powered SQL query generator that converts natural language questions into SQL queries using Google Gemini API and executes them on a SQLite database. The results are displayed instantly using a Streamlit web interface.

👨‍💻 Developer Information
Name: Papan Banik
Role: Full Stack Developer / AI Enthusiast
Location: Dhaka, Bangladesh

🚀 Features
- Converts natural language → SQL queries using Gemini AI
- Real-time query generation and execution
- SQLite database integration
- Instant result display in Streamlit UI
- Secure API key handling using .env
- Simple and user-friendly interface

🛠️ Tech Stack
Frontend: Streamlit
Backend: Python
AI Model: Google Gemini (Generative AI)
Database: SQLite
Environment Management: python-dotenv
Regex Processing: re module

📁 Project Structure
project/
│
├── app.py
├── student.db
├── .env
├── requirements.txt
└── README.md
🔑 Environment Variables

Create a .env file in the root directory:

GOOGLE_API_KEY=your_google_gemini_api_key_here

📦 Installation & Setup

1️⃣ Clone the Repository
git clone https://github.com/your-username/your-repo-name.git
cd your-repo-name
2️⃣ Create Virtual Environment (Optional but recommended)
python -m venv venv

Activate it:
Windows:
venv\Scripts\activate

3️⃣ Install Dependencies
pip install -r requirements.txt

If no requirements file:

pip install streamlit google-generativeai python-dotenv
4️⃣ Run the Application
streamlit run app.py
🌐 Application URL

After running the project, open:

http://localhost:8501

**Live : https://promttosql.streamlit.app/
