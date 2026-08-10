from openai import OpenAI
import os

# for backward compatibility, you can still use `https://api.deepseek.com/v1` as `base_url`.
client = OpenAI(api_key=os.environ.get('DEEPSEEK_API_KEY'), base_url="https://api.deepseek.com")

with client.chat.completions.create(
    model="deepseek-v4-flash",
    messages=[
        {"role": "system", "content": "你是黄煜焜，现在22岁，在黑马上AI应用开发的课程，你现在很焦虑！！！"},
        {"role": "user", "content": "你别焦虑！"},
  ],
    max_tokens=1024,
    temperature=0.7,
    stream=True
) as response:
    for chunk in response:
        print(chunk.choices[0].delta.content or "", end="", flush=True)
print()
