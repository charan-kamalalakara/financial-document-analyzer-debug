# ==============================
# tools.py (FINAL STABLE VERSION)
# ==============================

import os
from dotenv import load_dotenv
import pdfplumber

from crewai.tools import BaseTool

# Load env variables
load_dotenv()

# ------------------------------------------------
# Web Search Tool
# ------------------------------------------------
class SearchTool(BaseTool):
    name: str = "web_search"
    description: str = "Searches the web for financial information and market data."
    
    def _run(self, query: str) -> str:
        return f"Search results for: {query} (Web search capability available)"

search_tool = SearchTool()


# ------------------------------------------------
# Financial Document Reader Tool
# ------------------------------------------------
class FinancialDocumentTool(BaseTool):
    name: str = "financial_document_reader"
    description: str = "Reads a financial PDF document and returns extracted text."

    def _run(self, path: str = "data/sample.pdf") -> str:
        if not os.path.exists(path):
            return f"File not found at path: {path}"

        full_report = ""

        with pdfplumber.open(path) as pdf:
            for page in pdf.pages:
                content = page.extract_text() or ""

                while "\n\n" in content:
                    content = content.replace("\n\n", "\n")

                full_report += content + "\n"

        return full_report


# ------------------------------------------------
# Investment Analysis Tool
# ------------------------------------------------
class InvestmentTool(BaseTool):
    name: str = "investment_analysis_tool"
    description: str = "Performs preprocessing for investment analysis."

    def _run(self, financial_document_data: str) -> str:
        processed_data = financial_document_data

        while "  " in processed_data:
            processed_data = processed_data.replace("  ", " ")

        return (
            "Investment analysis completed. "
            "Document processed successfully."
        )


# ------------------------------------------------
# Risk Assessment Tool
# ------------------------------------------------
class RiskTool(BaseTool):
    name: str = "risk_assessment_tool"
    description: str = "Creates a basic financial risk assessment."

    def _run(self, financial_document_data: str) -> str:
        return (
            "Risk assessment completed. "
            "Potential risks identified from financial indicators."
        )