# API
# 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

from openai import OpenAI
client = OpenAI(api_key='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')

inp = ""
while inp != "exit":
    inp = input()
    completion = client.chat.completions.create(
        model="gpt-4o",
        messages=[
            {"role": "system", "content": 
             "You have one goal, provide youtube video links to what ever related piece of audio I give you."},
            {
                "role": "user",
                "content": inp
            }
        ]
    )
    print(completion.choices[0].message.content)

print("Chat ended.")
