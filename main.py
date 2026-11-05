from commons import client_connection



# with client: 
#     response = client.chat.send(
#         model = "gpt-4o-mini",
#         messages = [
#             {"role": "system", "content": "You are a helpful assistant."},
#             {"role": "user", "content": "Write a short poem about the ocean."}
#         ],
#         max_tokens = 1000
#     )

#     print(response.choices[0].message.content)

client = client_connection()

while True:
    user_input = input("You: ")
    if user_input.lower() == "exit":
        break

    with client.messages.stream(
        model='claude-haiku-4-5',
        system="AI Agent",
        messages=[{"role": "user", "content": user_input}],
        max_tokens=1000,) as stream:

        for chunk in stream.text_stream:
            print(chunk, end="", flush=True)
        
    print('\n')



