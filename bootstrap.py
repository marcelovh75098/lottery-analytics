from database.db import init_db, get_total_draws, insert_draw


def bootstrap_if_empty():
    """
    Garantiza que el sistema NUNCA arranque vacío.
    Si no hay datos → crea seed mínimo.
    """

    init_db()

    total = get_total_draws()

    if total > 0:
        return {"status": "ok", "total": total}

    # 🔥 SEED MÍNIMO (OBLIGATORIO PARA QUE NO ROMPA)
    seed = [
        ("2024-01-01", 1, 2, 3, 4, 5, 6),
        ("2024-01-02", 6, 7, 8, 9, 10, 11),
        ("2024-01-03", 11, 12, 13, 14, 15, 16),
        ("2024-01-04", 16, 17, 18, 19, 20, 21),
        ("2024-01-05", 21, 22, 23, 24, 25, 26),
    ]

    inserted = 0

    for d in seed:
        insert_draw(*d)
        inserted += 1

    return {"status": "bootstrapped", "inserted": inserted}
