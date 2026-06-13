from database.db import init_db, get_total_draws


def bootstrap_if_empty():

    init_db()

    total = get_total_draws()

    return {
        "status": "ok",
        "total_draws": total
    }
