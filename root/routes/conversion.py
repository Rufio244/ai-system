from fastapi import APIRouter
from db import SessionLocal
from models import Conversion
from root.bandit import update

router = APIRouter()

def compute_reward(amount: float):
    # ปรับสูตรได้
    return amount  # เน้นเงินจริงตรง ๆ

@router.post("/conversion")
def conversion(post_id: str, amount: float, strategy: str):
    db = SessionLocal()

    # บันทึกรายได้
    db.add(Conversion(post_id=post_id, amount=amount))
    db.commit()
    db.close()

    # คำนวณ reward แล้วสอน Root
    reward = compute_reward(amount)
    update(strategy, reward)

    return {"status": "ok", "reward": reward}
