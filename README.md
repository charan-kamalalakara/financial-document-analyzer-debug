# Financial Document Analyzer – Debug Challenge (CrewAI)

## 📌 Assignment Overview

This project is a **financial document analysis system** built using **CrewAI agentic architecture**.  
The system analyzes financial PDFs and generates structured insights such as:

- Financial performance analysis
- Investment recommendations
- Risk assessment
- Market insights

The original repository intentionally contained multiple issues including **deterministic bugs** and **inefficient prompt design**.  
This submission fixes those issues and delivers a fully working system.

---

## ✅ Final Working Features

- Upload financial documents (PDF format)
- Multi-agent AI analysis using CrewAI
- Structured financial insights generation
- Investment recommendations
- Risk evaluation
- FastAPI backend with interactive Swagger UI
- Gemini LLM integration

---

## 🧠 System Architecture

```
User Upload (PDF)
        ↓
FastAPI Endpoint (/analyze)
        ↓
CrewAI Orchestrator
        ↓
Financial Analyst Agent
        ↓
Custom Tools (PDF Reader + Analysis)
        ↓
Gemini LLM
        ↓
Structured Financial Insights
```

### Core Components

| Component | Purpose |
|---|---|
| FastAPI | API server and file upload handling |
| CrewAI | Agent orchestration |
| Gemini 1.5 Flash | LLM reasoning engine |
| Custom Tools | PDF parsing & analysis |
| dotenv | Environment configuration |

---

## 🐛 Bugs Found & Fixes Implemented

This project originally contained multiple intentional failures.  
Below are the major issues identified and resolved.

---

### 1️⃣ Dependency Conflicts (Critical Startup Failure)

**Problem**
- `requirements.txt` contained incompatible package versions.
- CrewAI required newer versions of `pydantic`, `onnxruntime`, and `opentelemetry`.

**Fix**
- Resolved version conflicts.
- Removed unnecessary pinned dependencies.
- Installed only required runtime libraries.

---

### 2️⃣ CrewAI API Migration Issues

**Problem**
- Tools were implemented as plain functions.
- CrewAI v0.130 requires `BaseTool` objects.

**Fix**
- Refactored tools into proper CrewAI tool classes.
- Updated agent and task configurations to use tool instances.

---

### 3️⃣ Broken Tool Integration

**Problem**
```
FinancialDocumentTool.read_data_tool
```
Referenced deprecated class methods.

**Fix**
```
tools=[FinancialDocumentTool()]
```
Updated to modern CrewAI tool usage.

---

### 4️⃣ Incorrect Agent Prompts (Inefficient & Unsafe)

**Problem**
Agents were intentionally designed to:
- hallucinate financial data
- ignore documents
- produce fake URLs
- give unsafe investment advice

**Fix**
- Rewrote prompts to:
  - rely strictly on document evidence
  - produce structured outputs
  - reduce token waste
  - follow realistic financial reasoning

---

### 5️⃣ Task Configuration Errors

**Problem**
- All tasks used the same agent incorrectly.
- Tasks ignored user query context.

**Fix**
- Proper agent-task separation.
- Structured expected outputs.
- Context-aware execution.

---

### 6️⃣ FastAPI Runtime Issues

**Problems**
- Hidden exceptions returning generic 500 errors.
- File path not passed into Crew workflow.

**Fix**
- Added traceback debugging.
- Correctly passed inputs:
```
inputs={"query": query, "file_path": file_path}
```

---

### 7️⃣ Environment Configuration Issues

**Problems**
- `.env` not consistently loaded.
- API key not injected into CrewAI LLM.

**Fix**
- Enabled dotenv loading.
- Explicit API key injection into LLM configuration.

---

### 8️⃣ Gemini Integration Errors

**Problems**
- Incorrect model naming.
- LiteLLM routing to Vertex AI instead of Gemini API.
- Missing authentication dependencies.

**Fix**
- Correct Gemini model configuration.
- Installed required authentication libraries.
- Ensured API key based authentication.

---

### 9️⃣ Missing Runtime Dependencies

**Problem**
FastAPI file uploads failed.

**Fix**
Installed:
```
python-multipart
```

---

## ⚙️ Setup Instructions

### 1. Clone Repository

```bash
git clone <your-repo-url>
cd financial-document-analyzer-debug
```

---

### 2. Create Virtual Environment (Python 3.10)

```bash
python -m venv venv
venv\Scripts\activate
```

---

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

---

### 4. Configure Environment Variables

Create a `.env` file:

```
GOOGLE_API_KEY=YOUR_GEMINI_API_KEY
```

Get API key from:
https://aistudio.google.com/app/apikey

---

### 5. Run Server

```bash
uvicorn main:app --reload
```

---

## 🚀 API Usage

Open Swagger UI:

```
http://127.0.0.1:8000/docs
```

### POST `/analyze`

Upload a financial PDF and provide a query.

**Example Query**
```
Analyze financial performance and investment risks
```

**Response**
```json
{
  "status": "success",
  "analysis": "...AI generated financial insights..."
}
```

---

## 📄 Sample Document

You may test using:

- Tesla Investor Reports
- Annual Reports (Apple, Infosys, Reliance, etc.)
- Any financial statement PDF

---

## 🧩 Project Structure

```
.
├── agents.py        # CrewAI agent definitions
├── task.py          # Task workflows
├── tools.py         # Custom analysis tools
├── main.py          # FastAPI server
├── requirements.txt
├── data/
└── README.md
```

---

## ⭐ Improvements Made Beyond Fixes

- Cleaner agent reasoning flow
- Reduced hallucination risk
- Improved prompt efficiency
- Stable Gemini integration
- Production-ready API execution

---

## 🧪 Future Enhancements (Bonus Scope)

- Queue worker support (Celery / Redis)
- Database storage for analysis history
- Multi-agent parallel execution
- RAG-based financial knowledge retrieval

---

## 👨‍💻 Author

Submission for **GenAI Engineering Intern – VWO Debug Challenge**

This implementation focuses on debugging, system stabilization, and production-ready agent orchestration using CrewAI.

---