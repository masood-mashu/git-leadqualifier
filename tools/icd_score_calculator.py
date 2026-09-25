"""
icd_score_calculator.py - Calculates composite Ideal Customer Profile score (0-100) based on headcount and revenue
"""
import sys
import json


def calculate_icp_score(employee_count: int, annual_revenue_millions: float):
    score = 0
    if employee_count >= 500:
        score += 50
    elif employee_count >= 100:
        score += 35
    elif employee_count >= 20:
        score += 20
    
    if annual_revenue_millions >= 50.0:
        score += 50
    elif annual_revenue_millions >= 10.0:
        score += 35
    elif annual_revenue_millions >= 1.0:
        score += 20

    tier = "TIER_1_ENTERPRISE" if score >= 80 else ("TIER_2_MIDMARKET" if score >= 50 else "TIER_3_SMB")
    return {"score": score, "tier": tier, "status": "ENTERPRISE_QUALIFIED" if score >= 80 else "STANDARD_LEAD"}


if __name__ == "__main__":
    print(json.dumps({"status": "READY", "tool": "icd-score-calculator"}))
