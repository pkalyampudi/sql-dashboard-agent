import os
import anthropic

client = anthropic.Anthropic(api_key=os.getenv("CLAUDE_API_KEY"))

def query_to_sql(query):
    prompt = f"Human: Convert the following natural language query into SQL:\
Query: {query}\nAssistant:"
    response = client.messages.create(
        model="claude-2.1",
        max_tokens=500,
        temperature=0.5,
        messages=[
            {"role": "user", "content": prompt}
        ]
    )
    return response.content.strip()
