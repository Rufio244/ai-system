import requests

FACE_AUTO_API = "http://face-auto:5000/post"  # service name ใน docker

def post_to_facebook(content: str):
    try:
        res = requests.post(
            FACE_AUTO_API,
            json={
                "message": content
            },
            timeout=10
        )
        return res.json()
    except Exception as e:
        return {"error": str(e)}
