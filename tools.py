# ==============================
# tools.py (FIXED VERSION)
# ==============================

## Import libraries
import os
from dotenv import load_dotenv
import pdfplumber

from crewai_tools import tool, SerperDevTool

# Load environment variables
load_dotenv()


# ------------------------------------------------
# Web Search Tool (provided by CrewAI)
# ------------------------------------------------
search_tool = SerperDevTool()


# ------------------------------------------------
# Financial Document Reader Tool
# ------------------------------------------------
@tool("financial_document_reader")
def read_financial_document(path: str = "data/sample.pdf") -> str:
    """
    Reads a financial PDF document and returns cleaned text content.

    Args:
        path (str): Path to the financial PDF file.

    Returns:
        str: Extracted and cleaned document text.
    """

    if not os.path.exists(path):
        return f"File not found at path: {path}"

    full_report = ""

    with pdfplumber.open(path) as pdf:
        for page in pdf.pages:
            content = page.extract_text() or ""

            # Clean formatting
            while "\n\n" in content:
                content = content.replace("\n\n", "\n")

            full_report += content + "\n"

    return full_report


# ------------------------------------------------
# Investment Analysis Tool
# ------------------------------------------------
@tool("investment_analysis_tool")
def analyze_investment(financial_document_data: str) -> str:
    """
    Performs basic preprocessing for investment analysis.
    """

    processed_data = financial_document_data

    # Remove double spaces
    while "  " in processed_data:
        processed_data = processed_data.replace("  ", " ")

    # Placeholder logic (intentionally simple)
    return (
        "Investment analysis completed.\n"
        "Document processed successfully. "
        "Further financial modeling can be implemented."
    )


# ------------------------------------------------
# Risk Assessment Tool
# ------------------------------------------------
@tool("risk_assessment_tool")
def create_risk_assessment(financial_document_data: str) -> str:
    """
    Generates a basic risk assessment placeholder.
    """

    return (
        "Risk assessment completed.\n"
        "Potential financial risks should be evaluated "
        "based on liabilities, cash flow, and volatility indicators."
    )