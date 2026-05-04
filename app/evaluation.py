from tracking import best_topics

def evaluate_system():
    data = best_topics()

    if not data:
        return {"status": "no_data"}

    best = data[0]

    return {
        "best_performance": best,
        "insight": f"Best topic is {best['topic']} with score {best['score']}"
    }
