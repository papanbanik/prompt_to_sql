from dotenv import load_dotenv
load_dotenv()  # Load environment variables

import streamlit as st
import os
import sqlite3
import re
import google.generativeai as genai

# Configure Gemini API key
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

# --- Function: Get SQL query from Gemini ---
def get_gemini_response(question, prompt):
    model = genai.GenerativeModel("models/gemini-2.5-pro")
    response = model.generate_content([prompt[0], question])
    sql_query = response.text.strip()

    # ✅ Clean output: remove code fences or explanations
    sql_query = re.sub(r"```.*?```", "", sql_query, flags=re.DOTALL)
    sql_query = re.sub(r"(?i).*?(SELECT\s+.+)", r"\1", sql_query, flags=re.DOTALL)
    sql_query = sql_query.strip().strip('"').strip("'").strip()

    return sql_query


# --- Function: Execute SQL query ---
def read_sql_query(sql, db):
    try:
        conn = sqlite3.connect(db)
        cur = conn.cursor()
        cur.execute(sql)
        rows = cur.fetchall()
        conn.close()
        return rows
    except Exception as e:
        return [("❌ SQL Error:", str(e))]


# --- Prompt ---
prompt = [
    """
    You are an expert at converting English questions into SQL queries.
    The database name is STUDENT with columns: NAME, CLASS, SECTION, MARKS.

    Rules:
    - Output only the SQL query, nothing else.
    - Use correct uppercase column names.
    - Do not add ```sql or explanations.
    Examples:
    1. How many entries of records are present?
       → SELECT COUNT(*) FROM STUDENT;
    2. Tell me all the students in section A.
       → SELECT * FROM STUDENT WHERE SECTION = 'A';
    """
]


# --- Streamlit UI ---
st.set_page_config(page_title="AI SQL Query Generator", page_icon="🤖")
st.title("🤖 Gemini SQL Assistant")
st.write("Ask a question about the student database, and I’ll run the SQL query for you!")

question = st.text_input("Enter your question:")

if st.button("Ask"):
    if question.strip():
        with st.spinner("Thinking..."):
            sql_query = get_gemini_response(question, prompt)
            st.code(sql_query, language="sql")

            result = read_sql_query(sql_query, "student.db")

            st.subheader("Result:")
            if len(result) == 0:
                st.info("No matching records found.")
            else:
                for row in result:
                    st.write(row)
    else:
        st.warning("Please enter a question.")
