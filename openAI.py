import openai

# Set your OpenAI API key
openai.api_key = "API_KEY"

def get_chat_completion(prompt):
    response = openai.Completion.create(
        engine="text-davinci-002",
        prompt=prompt,
        max_tokens=150
    )
    return response.choices[0].text.strip()

def main():
    # Initial conversation
    conversation = [
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": "Who won the world series in 2020?"},
        {"role": "assistant", "content": "The Los Angeles Dodgers won the World Series in 2020."},
        {"role": "user", "content": "Where was it played?"}
    ]

    # Continue the conversation
    prompt = "\n".join([f"{turn['role']}: {turn['content']}" for turn in conversation])
    response = get_chat_completion(prompt)

    # Display the AI's response
    print(f"Assistant: {response}")

if _name_ == "_main_":
    main()