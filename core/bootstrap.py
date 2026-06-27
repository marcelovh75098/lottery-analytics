from dataclasses import dataclass
from typing import Any


@dataclass
class AppContext:

    draws: Any
    features: Any
    strategies: Any
    portfolio: Any
    ranking: Any
    elite: Any
    report: Any
    metrics: Any


def initialize_system():

    """
    Punto único de inicialización.

    Toda la lógica de carga del sistema se centraliza aquí.

    app.py únicamente llamará esta función.
    """

    # ============================
    # IMPORTS DIFERIDOS
    # ============================

    # Se importan aquí para evitar
    # dependencias circulares.

    from database.database import init_database

    from engine.bootstrap import bootstrap_database

    from engine.feature_engineering import build_features

    from engine.portfolio import PortfolioEngine

    from engine.ranking import RankingEngine

    from engine.elite import EliteEngine

    from reports.report_builder import ReportBuilder

    from predictors.predictor import Predictor

    from database.repository import LotteryRepository

    # ============================
    # Base de datos
    # ============================

    init_database()

    bootstrap_database()

    repository = LotteryRepository()

    draws = repository.get_all_draws()

    # ============================
    # Features
    # ============================

    features = build_features(draws)

    # ============================
    # Predictor
    # ============================

    predictor = Predictor()

    predictions = predictor.predict(features)

    # ============================
    # Portfolio
    # ============================

    portfolio_engine = PortfolioEngine()

    portfolio = portfolio_engine.build(predictions)

    # ============================
    # Ranking
    # ============================

    ranking_engine = RankingEngine()

    ranking = ranking_engine.build()

    # ============================
    # Elite
    # ============================

    elite_engine = EliteEngine()

    elite = elite_engine.build(
        predictions=predictions,
        ranking=ranking
    )

    # ============================
    # Reporte
    # ============================

    report_builder = ReportBuilder()

    report = report_builder.build(
        elite=elite,
        portfolio=portfolio
    )

    metrics = {

        "total_draws": len(draws),

        "strategies": len(ranking),

        "predictions": len(predictions)

    }

    return AppContext(

        draws=draws,

        features=features,

        strategies=ranking,

        portfolio=portfolio,

        ranking=ranking,

        elite=elite,

        report=report,

        metrics=metrics

    )
