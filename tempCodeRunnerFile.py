while True:
    input_text = input("User:")
    response = kernel.respond(input_text)
    print("Bot:" + response)