from fastapi import APIRouter
from .engine import evaluate
from .registry import get_formula, set_formula
from .signals import get_signals

router = APIRouter()

@router.get("/root/score")
def score(mode: str = "default"):
    expr = get_formula(mode)
    signals = get_signals()
    value = evaluate(expr, signals)
    return {"mode": mode, "formula": expr, "signals": signals, "score": value}

@router.post("/root/formula")
def update(name: str, expr: str):
    set_formula(name, expr)
    return {"status": "updated", "name": name}
