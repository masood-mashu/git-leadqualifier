from crewai import Agent
def create_agent():
    return Agent(role='GitLeadQualifier', goal='Autonomous B2B Lead Scoring, Ideal Customer Profile (ICP) Matcher & Disposable Email Filter Agent', backstory='Autonomous agent', verbose=True)
