from dataclasses import dataclass
from typing import Any

import pandas as pd

from database.db import (
    init_db,
    get_all_draws,
    get_total_draws,
)

from engine.bootstrap import bootstrap_database
from engine.features import build_features


@dataclass
class AppContext:
    draws: Any
    dataframe: pd.DataFrame
    features: Any
    metrics: dict
    frequency_df: pd.DataFrame
    hot_numbers: pd.DataFrame
    cold_numbers: pd.DataFrame
    parity: list


def initialize_system() -> AppContext:
    """
    Inicializa Lottery Analytics.

    Este módulo únicamente prepara el contexto global que utilizará
    toda la interfaz de usuario.
    """

    # -------------------------------------------------------
    # Base de datos
    # -------------------------------------------------------

    init_db()
    bootstrap_database()

    draws = get_all_draws()

    # -------------------------------------------------------
    # DataFrame principal
    # -------------------------------------------------------

    dataframe = pd.DataFrame(
        draws,
        columns=[
            "n1",
            "n2",
            "n3",
            "n4",
            "n5",
            "superbalota",
        ],
    )

    # -------------------------------------------------------
    # Feature Engineering
    # -------------------------------------------------------

    features = build_features(draws)

    # -------------------------------------------------------
    # Frecuencias
    # -------------------------------------------------------

    numbers = []

    for column in ["n1", "n2", "n3", "n4", "n5"]:
        numbers.extend(dataframe[column].tolist())

    frequency = (
        pd.Series(numbers)
        .value_counts()
        .sort_index()
    )

    frequency_df = pd.DataFrame(
        {
            "numero": frequency.index,
            "frecuencia": frequency.values,
        }
    )

    # -------------------------------------------------------
    # Hot / Cold Numbers
    # -------------------------------------------------------

    hot_numbers = (
        frequency_df
        .sort_values(
            "frecuencia",
            ascending=False,
        )
        .head(15)
        .reset_index(drop=True)
    )

    cold_numbers = (
        frequency_df
        .sort_values(
            "frecuencia",
            ascending=True,
        )
        .head(15)
        .reset_index(drop=True)
    )

    # -------------------------------------------------------
    # Paridad
    # -------------------------------------------------------

    pares = sum(1 for n in numbers if n % 2 == 0)
    impares = len(numbers) - pares

    parity = [pares, impares]

    # -------------------------------------------------------
    # Métricas generales
    # -------------------------------------------------------

    metrics = {
        "total_draws": get_total_draws(),
        "numbers_analyzed": len(numbers),
        "strategies": 0,
        "predictions": 0,
        "database_status": "ONLINE",
    }

    # -------------------------------------------------------
    # Contexto global
    # -------------------------------------------------------

    return AppContext(
        draws=draws,
        dataframe=dataframe,
        features=features,
        metrics=metrics,
        frequency_df=frequency_df,
        hot_numbers=hot_numbers,
        cold_numbers=cold_numbers,
        parity=parity,
    )
