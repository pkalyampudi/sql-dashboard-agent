### 🧠 SQL to Dashboard AI Agent (Powered by Claude) ###
This project enables users to generate interactive dashboards from SQL databases using natural language queries — no SQL knowledge required!

### 🔍 What It Does ###
Converts plain English questions into SQL queries using Claude (Anthropic API)
Executes queries on a connected SQL database
Automatically generates visualizations using Plotly
Displays results in an interactive Streamlit dashboard

### ⚙️ Tech Stack ###
Claude (Anthropic API) for natural language understanding
SQLAlchemy for database connectivity
Pandas for data manipulation
Plotly for charting
Streamlit for UI

### 🚀 How to Use

Clone the repo:

git clone https://github.com/pkalyampudi/sql-dashboard-agent.git
cd sql-to-dashboard-ai-agent

Install dependencies:

pip install -r requirements.txt

Set your Claude API key:

export CLAUDE_API_KEY=your_api_key_here

Run the app:

streamlit run app.py

### 📊 Example Query
“Show me the total sales by region for Q1”

The app will:

Generate the SQL query
Run it on your database
Display a bar chart with the results
