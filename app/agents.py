import openai
import os

openai.api_key = os.getenv("OPENAI_API_KEY")

def run_agent(prompt):
    response = openai.ChatCompletion.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": "You are an autonomous business AI."},
            {"role": "user", "content": prompt}
        ]
    )
    return response.choices[0].message["content"]
