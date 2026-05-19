# 🏫 ProviBot - FCPC AI Campus Assistant
ProviBot is an AI-powered campus buddy for First City Providential College (FCPC). Built using Python, Streamlit, and the Google Gemini API, it provides intelligent, context-aware answers to student inquiries based entirely on a verified institutional knowledge base.

## 🚀 How to Run the Project Locally
Follow these step-by-step instructions to set up and run ProviBot on your local machine.

### Prerequisites
Make sure you have the following installed on your computer:
* **Python (v3.9 or higher)**
* **Git**
* A code editor like **VS Code**

### Step 1: Clone the Repository
Open your terminal or Git Bash, navigate to the folder where you want to save the project, and run:
git clone [https://github.com/Keith-Nicole/FCPC-Chatbot.git](https://github.com/Keith-Nicole/FCPC-Chatbot.git)
cd FCPC-Chatbot

### Step 2: Install Dependencies
Install the required Python frameworks and libraries listed in the `requirements.txt` file by running:
pip install -r requirements.txt

### Step 3: Set Up Your Private API Key (Crucial)
Because the original developer's configuration files are hidden for security, **the app will crash unless you set up your own local API key vault.**

1. Create a brand new file in the root directory and name it exactly: `.env`
2. Go to [Google AI Studio](https://aistudio.google.com/) and sign in with your Gmail account.
3. Click **Create API Key**, copy the generated key, and paste it inside your new `.env` file exactly like this:
GEMINI_API_KEY="your_actual_api_key_here"

### Step 4: Run the Application
Start the Streamlit local web server by running the following command in your terminal:
streamlit run app.py

A local web browser tab should automatically open at `http://localhost:8501`, displaying the active ProviBot chat interface. You're all set!

---

## 🛠️ Project Structure

* `app.py` - The core application file handling the UI, state retention, and API logic.
* `knowledge_base.txt` - The primary text asset containing all verified FCPC rules and paths.
* `requirements.txt` - The library installation map required for both local and cloud setups.
* `.gitignore` - Prevents local `.env` files from leaking into the public cloud environment.

```

