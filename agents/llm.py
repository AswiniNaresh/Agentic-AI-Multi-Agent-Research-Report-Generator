import requests
from config import GROQ_API_KEY

def groq_llm(prompt):
    response = requests.post(
        "https://api.groq.com/openai/v1/chat/completions",
        headers={
            "Authorization": f"Bearer {GROQ_API_KEY}",
            "Content-Type": "application/json"
        },
        json={
            "model": "llama-3.3-70b-versatile",
            "messages": [{"role": "user", "content": prompt}]
        }
    )
    
    # Check if request was successful
    if response.status_code != 200:
        raise Exception(f"Groq API error: {response.status_code} - {response.text}")
    
    # Parse response and check for error field
    data = response.json()
    if "error" in data:
        raise Exception(f"Groq API error: {data['error']}")
    
    if "choices" not in data:
        raise Exception(f"Unexpected Groq API response format: {data}")
    
    return data["choices"][0]["message"]["content"]