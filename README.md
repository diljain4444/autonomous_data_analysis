
# 🧠 Autonomous Data Analysis Agent

An AI-powered autonomous data analysis system that allows users to upload a CSV file, ask natural language questions, and receive dynamic data insights and visualizations generated through executable Python code.

This project combines **Streamlit**, **LangChain**, **LangGraph**, and **LLM-based code generation** to simulate the behavior of an intelligent data analyst.



## 🚀 Features

* 📂 Upload any CSV file
* 💬 Ask natural language questions about the data
* 🧑‍💻 LLM generates **pure executable Python code**
* 📊 Automatic data analysis and visualizations
* 🧠 Agent-based workflow using **LangGraph**
* 🔒 Safe execution with strict environment rules
* 🖼️ Plot rendering using Matplotlib
* 🧪 Error handling for invalid queries or columns

---

## 🛠️ Tech Stack

### Frontend

* **Streamlit**
* **Pandas**
* **NumPy**
* **Matplotlib**

### Backend / Agent

* **LangChain**
* **LangGraph**
* **HuggingFace LLM (Llama 3.1 8B Instruct)**



## 🧩 Project Architecture


├── frontend.py                # Streamlit UI
├── data_analysis_backend.py   # LangGraph agent workflow
├── requirements.txt
└── README.md



## 🧠 How It Works

1. User uploads a CSV file
2. The system extracts column names
3. User asks a question in natural language
4. An LLM generates **pure Python code** based on strict rules
5. The code is executed using `exec()` on the DataFrame
6. Results (plots / outputs) are displayed in the UI



## 🧪 Prompt Safety Rules

The AI-generated code follows strict constraints:

* ✅ Allowed libraries only:

  * `pandas`
  * `numpy`
  * `matplotlib`
* ❌ No file read/write operations
* ❌ No Streamlit usage in generated code
* ❌ No imports
* 📊 All plots must end with:

  ```python
  fig
  ```
* ❗ Invalid column references raise explicit errors

---

## 📈 Example Queries

* “Show the correlation matrix”
* “Plot average sales by category”
* “Find top 5 rows with highest profit”
* “Check missing values in each column”
* “Plot histogram of age column”


## ⚙️ Installation & Setup

```bash
git clone https://github.com/your-username/autonomous-data-analysis.git
cd autonomous-data-analysis
pip install -r requirements.txt
streamlit run frontend.py
```



## 🧠 Learning Outcomes

* Building agent-based systems with LangGraph
* Using LLMs for **code generation**
* Safe execution of AI-generated Python code
* Prompt engineering for structured outputs
* Designing autonomous analytical workflows

---

## 📌 Future Improvements

* Conversation memory across sessions
* Downloadable plots and code
* Advanced chart types (Seaborn)
* Auto-insight generation
* Multi-file analysis
* Cloud deployment (Docker / DigitalOcean)

---

## 👤 Author

**Dil Jain**
B.Tech – Artificial Intelligence & Data Science
Focused on AI Agents, Data Science, and Backend Systems

---

## ⭐ Final Note

This project demonstrates how LLMs can be used as **autonomous analytical agents**, bridging the gap between human questions and machine-executed insights.

