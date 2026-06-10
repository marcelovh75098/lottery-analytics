from database.db import get_total_draws
from ingestion.seed_loader import load_seed


def ensure_data(min_rows=30):

    total = get_total_draws()

    # =========================
    # YA HAY DATA
    # =========================
    if total >= min_rows:
        return {
            "status": "ok",
            "total": total
        }

    # =========================
    # NO HAY DATA → USAR SEED
    # =========================
    inserted = load_seed()

    return {
        "status": "ok",
        "inserted": inserted,
        "total": get_total_draws()
    }
