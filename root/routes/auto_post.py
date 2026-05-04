from fastapi import APIRouter
from root.engine import decide
from monetization.select import choose_offer

router = APIRouter()

def generate_content(topic: str, strategy: str, link: str):
    # คุณสามารถต่อกับ AI service จริงได้
    return f"🔥 {topic}\n\nวิธีทำเงินด้วย AI ตอนนี้!\n👉 {link}"

@router.post("/auto/post")
def auto_post(topic: str = "AI making money"):
    d = decide()
    strategy = d["choice"]

    offer = choose_offer(strategy)
    if not offer:
        return {"error": "no offer found"}

    link = f"http://localhost:8000/go/{offer.id}?post_id=auto_{strategy}"
    content = generate_content(topic, strategy, link)

    return {
        "strategy": strategy,
        "offer_id": offer.id,
        "content": content,
        "link": link,
        "score": d["score"]
    }
