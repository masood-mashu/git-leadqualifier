"""
eval_predictability.py - Checkpoint 02 Benchmark Suite for GitLeadQualifier.
"""
import os, sys, unittest
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from tools.disposable_email_detector import *
from tools.icd_score_calculator import *
from tools.round_robin_assigner import *
from tools.phone_format_validator import *

class TestGitLeadQualifierPredictability(unittest.TestCase):

    def test_01_detect_disposable_domain(self):
        res = detect_disposable_email("user@mailinator.com")
        self.assertTrue(res["is_disposable"])
        self.assertFalse(res["corporate_lead"])

    def test_02_icp_score_enterprise(self):
        res = calculate_icp_score(employee_count=1000, annual_revenue_millions=100.0)
        self.assertEqual(res["tier"], "TIER_1_ENTERPRISE")
        self.assertEqual(res["score"], 100)

    def test_03_phone_e164_valid(self):
        res = validate_phone_e164("+14155552671")
        self.assertTrue(res["valid_e164"])


if __name__ == "__main__":
    unittest.main()
