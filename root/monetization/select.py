from db import SessionLocal
from models import Offer

# map strategy → type
STRATEGY_MAP = {
    "aggressive": "affiliate",
    "balanced": "product",
    "safe": "subscription"
}

def choose_offer(strategy: str):
    db = SessionLocal()
    otype = STRATEGY_MAP.get(strategy, "product")
    offer = db.query(Offer).filter(Offer.type == otype).order_by(Offer.id.desc()).first()
    db.close()
    return offer
