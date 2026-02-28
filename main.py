from fastapi import FastAPI, File, UploadFile, Form, HTTPException
import os
import uuid
import traceback

from crewai import Crew, Process
from agents import financial_analyst
from task import analyze_financial_document as analyze_task

app = FastAPI(title="Financial Document Analyzer")


# ------------------------------------------------
# Crew Runner
# ------------------------------------------------
def run_crew(query: str, file_path: str):
    """Run CrewAI workflow"""

    financial_crew = Crew(
        agents=[financial_analyst],
        tasks=[analyze_task],
        process=Process.sequential,
    )

    # ✅ PASS BOTH query AND file path to agents/tools
    result = financial_crew.kickoff(
        inputs={
            "query": query,
            "file_path": file_path
        }
    )

    return result


# ------------------------------------------------
# Health Check
# ------------------------------------------------
@app.get("/")
async def root():
    return {"message": "Financial Document Analyzer API is running"}


# ------------------------------------------------
# Analyze Endpoint
# ------------------------------------------------
@app.post("/analyze")
async def analyze_financial_document(
    file: UploadFile = File(...),
    query: str = Form(
        default="Analyze this financial document for investment insights"
    ),
):

    file_id = str(uuid.uuid4())
    file_path = f"data/financial_document_{file_id}.pdf"

    try:
        os.makedirs("data", exist_ok=True)

        # Save uploaded file
        with open(file_path, "wb") as f:
            content = await file.read()
            f.write(content)

        if not query:
            query = "Analyze this financial document for investment insights"

        # ✅ Run CrewAI
        response = run_crew(
            query=query.strip(),
            file_path=file_path
        )

        return {
            "status": "success",
            "query": query,
            "analysis": str(response),
            "file_processed": file.filename,
        }

    except Exception as e:
        # ✅ SHOW REAL ERROR IN TERMINAL
        traceback.print_exc()
        raise HTTPException(
            status_code=500,
            detail=f"Error processing financial document: {str(e)}",
        )

    finally:
        # Cleanup uploaded file
        if os.path.exists(file_path):
            try:
                os.remove(file_path)
            except Exception:
                pass


# ------------------------------------------------
# Local Run
# ------------------------------------------------
if __name__ == "__main__":
    import uvicorn

    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)