from openai import OpenAI
import os
from face_auto import post_to_facebook

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def run_agent(prompt):
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": "You are a marketing AI that creates viral Facebook posts."},
            {"role": "user", "content": prompt}
        ]
    )

    content = response.choices[0].message.content

    # 🔥 ส่งไป Face Auto
    post_result = post_to_facebook(content)

    return {
        "content": content,
        "post_result": post_result
    }
