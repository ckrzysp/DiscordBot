# API Testing

from openai import OpenAI
client = OpenAI(api_key='YOUR API HERE')

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
