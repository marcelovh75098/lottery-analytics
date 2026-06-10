from database.db import get_total_draws
from ingestion.seed_loader import load_seed


def ensure_bootstrap():

    total = get_total_draws()

    # 🔥 si no hay data, se inyecta seed institucional
    if total < 30:
        inserted = load_seed()
        return {
            "status": "bootstrapped",
            "inserted": inserted
        }

    return {
        "status": "ready",
        "total": total
    }
