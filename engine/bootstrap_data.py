from database.db import get_total_draws, insert_draw
from ingestion.seed_loader import load_seed


def ensure_bootstrap():
    """
    JUSTIFICACIÓN:
    Este es el "gatekeeper institucional".
    - Garantiza que el sistema NUNCA corra con dataset vacío.
    - Si no hay datos suficientes, activa seed dataset.
    - Simula comportamiento de sistemas cuantitativos reales.
    """

    total = get_total_draws()

    if total < 30:
        inserted = load_seed()

        return {
            "status": "bootstrapped",
            "inserted": inserted,
            "message": "Dataset inicial cargado automáticamente"
        }

    return {
        "status": "ready",
        "total": total,
        "message": "Dataset institucional válido"
    }
