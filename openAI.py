import openai

openai.api_key = "API_KEY"

def get_chat_completion(prompt):
    response = openai.Completion.create(
        engine="text-davinci-002",
        prompt=prompt,
        max_tokens=150
    )
    return response.choices[0].text.strip()

def main():
    conversation = [
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": "Who won the world series in 2020?"},
        {"role": "assistant", "content": "The Los Angeles Dodgers won the World Series in 2020."},
        {"role": "user", "content": "Where was it played?"}
    ]

    prompt = "\n".join([f"{turn['role']}: {turn['content']}" for turn in conversation])
    response = get_chat_completion(prompt)

    print(f"Assistant: {response}")

if _name_ == "_main_":
    main()