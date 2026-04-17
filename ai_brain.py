from openai import OpenAI

client = OpenAI(api_key="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")

def ask_ai(prompt):
    try:
        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {"role": "system", "content": "You are a helpful AI assistant."},
                {"role": "user", "content": prompt}
            ]
        )
        return response.choices[0].message.content

    except Exception as e:
        return f"AI Error: {str(e)}"