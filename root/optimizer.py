import random

def mutate(expr: str):
    # ปรับค่าน้ำหนักเล็กน้อย (toy example)
    return expr.replace("0.6", str(round(0.6 + random.uniform(-0.1, 0.1), 2)))

def optimize(current_expr, history_scores):
    # เลือกสูตรที่ให้ผลลัพธ์ดีขึ้น (heuristic)
    candidate = mutate(current_expr)
    return candidate
