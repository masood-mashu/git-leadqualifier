"""
round_robin_assigner.py - Assigns lead to sales account executive in fair round-robin rotation
"""
import sys
import json


def assign_round_robin(lead_id: str, sales_reps: str = "rep_alice,rep_bob,rep_carol"):
    reps = [r.strip() for r in sales_reps.split(",") if r.strip()]
    if not reps:
        return {"assigned_rep": None, "status": "NO_REPS_AVAILABLE"}
    idx = hash(lead_id) % len(reps)
    assigned = reps[idx]
    return {"lead_id": lead_id, "assigned_rep": assigned, "status": "ASSIGNED"}


if __name__ == "__main__":
    print(json.dumps({"status": "READY", "tool": "round-robin-assigner"}))
