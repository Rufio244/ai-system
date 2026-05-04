import requests

BASE_URL = "http://api:8000"

def test_api():
    results = {}

    try:
        r = requests.get(f"{BASE_URL}/")
        results["root"] = r.status_code == 200
    except:
        results["root"] = False

    try:
        r = requests.get(f"{BASE_URL}/capabilities")
        results["capabilities"] = r.status_code == 200
    except:
        results["capabilities"] = False

    try:
        r = requests.post(f"{BASE_URL}/post", params={"message": "test"})
        results["post"] = r.status_code == 200
    except:
        results["post"] = False

    return results
