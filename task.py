# ==============================
# task.py (FIXED + OPTIMIZED)
# ==============================

from crewai import Task

from agents import (
    financial_analyst,
    verifier,
    investment_advisor,
    risk_assessor
)

from tools import FinancialDocumentTool


# ------------------------------------------------
# Document Verification Task
# ------------------------------------------------
verification = Task(
    description=(
        "Verify whether the uploaded file contains financial information. "
        "Read the document carefully and determine if it includes financial "
        "statements, numerical data, or business-related reporting."
    ),
    expected_output=(
        "A clear validation result stating whether the document is financial "
        "in nature, along with a short justification."
    ),
    agent=verifier,
    tools=[FinancialDocumentTool()],
    async_execution=False,
)


# ------------------------------------------------
# Financial Analysis Task
# ------------------------------------------------
analyze_financial_document = Task(
    description=(
        "Analyze the financial document provided and extract key insights "
        "such as revenue trends, profitability indicators, and financial health. "
        "Base conclusions strictly on document content."
    ),
    expected_output=(
        "Structured financial analysis including:\n"
        "- Key financial metrics\n"
        "- Observed trends\n"
        "- Important highlights from the document"
    ),
    agent=financial_analyst,
    tools=[FinancialDocumentTool()],
    async_execution=False,
)


# ------------------------------------------------
# Investment Recommendation Task
# ------------------------------------------------
investment_analysis = Task(
    description=(
        "Based on the financial analysis results, provide responsible "
        "investment recommendations. Suggestions must align with the "
        "financial performance observed in the document."
    ),
    expected_output=(
        "Investment recommendations including:\n"
        "- Potential opportunities\n"
        "- Supporting reasoning\n"
        "- Conservative risk-aware suggestions"
    ),
    agent=investment_advisor,
    tools=[FinancialDocumentTool()],
    async_execution=False,
)


# ------------------------------------------------
# Risk Assessment Task
# ------------------------------------------------
risk_assessment = Task(
    description=(
        "Evaluate financial risks present in the analyzed document. "
        "Consider liquidity, debt exposure, volatility, and operational risks."
    ),
    expected_output=(
        "Risk assessment report including:\n"
        "- Identified risks\n"
        "- Severity level\n"
        "- Possible mitigation strategies"
    ),
    agent=risk_assessor,
    tools=[FinancialDocumentTool()],
    async_execution=False,
)