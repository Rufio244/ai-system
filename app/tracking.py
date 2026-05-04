success_log = []

def track_success(topic, score):
    success_log.append({
        "topic": topic,
        "score": score
    })

def best_topics():
    return sorted(success_log, key=lambda x: x["score"], reverse=True)
