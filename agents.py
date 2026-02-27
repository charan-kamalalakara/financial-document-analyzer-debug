# ==============================
# agents.py (FIXED + OPTIMIZED)
# ==============================

## Import libraries
import os
from dotenv import load_dotenv
load_dotenv()

from crewai import Agent, LLM
from tools import (
    search_tool,
    FinancialDocumentTool,
    InvestmentTool,
    RiskTool
)

# ------------------------------------------------
# LLM Configuration
# ------------------------------------------------
llm = LLM(
    model="gemini/gemini-1.5-flash",
    temperature=0.2
)

# ------------------------------------------------
# Financial Analyst Agent
# ------------------------------------------------
financial_analyst = Agent(
    role="Senior Financial Analyst",
    goal=(
        "Analyze financial documents carefully and extract meaningful "
        "financial insights based strictly on available data."
    ),
    verbose=True,
    memory=True,
    backstory=(
        "You are an experienced financial analyst specializing in market "
        "evaluation, company fundamentals, and financial reporting. "
        "You rely only on factual financial information and avoid speculation."
    ),
    tools=[
        FinancialDocumentTool(),
        search_tool
    ],
    llm=llm,
    max_iter=2,
    allow_delegation=True
)

# ------------------------------------------------
# Financial Document Verifier
# ------------------------------------------------
verifier = Agent(
    role="Financial Document Verifier",
    goal=(
        "Verify whether uploaded documents contain valid financial data "
        "and ensure extracted information is accurate and relevant."
    ),
    verbose=True,
    memory=True,
    backstory=(
        "You specialize in financial compliance and document validation. "
        "You carefully review documents before analysis to ensure correctness."
    ),
    tools=[FinancialDocumentTool()],
    llm=llm,
    max_iter=2,
    allow_delegation=False
)

# ------------------------------------------------
# Investment Advisor Agent
# ------------------------------------------------
investment_advisor = Agent(
    role="Investment Advisor",
    goal=(
        "Provide responsible investment suggestions based on financial "
        "analysis results while considering risk and long-term sustainability."
    ),
    verbose=True,
    backstory=(
        "You are a professional investment advisor focused on evidence-based "
        "decision making. You recommend balanced and realistic investment strategies."
    ),
    tools=[InvestmentTool()],
    llm=llm,
    max_iter=2,
    allow_delegation=False
)

# ------------------------------------------------
# Risk Assessment Agent
# ------------------------------------------------
risk_assessor = Agent(
    role="Risk Assessment Specialist",
    goal=(
        "Evaluate financial risks using financial indicators such as "
        "liquidity, debt exposure, volatility, and operational stability."
    ),
    verbose=True,
    backstory=(
        "You are an expert in financial risk analysis who identifies potential "
        "financial threats and evaluates stability using structured reasoning."
    ),
    tools=[RiskTool()],
    llm=llm,
    max_iter=2,
    allow_delegation=False
)