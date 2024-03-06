import aiml


kernel = aiml.Kernel()
kernel.learn("std_startup.xml")
kernel.respond("LOAD AIML B")

while True:
    input_text = input("User:")
    response = kernel.respond(input_text)
    print("Bot:" + response)






# import aiml
# import subprocess

# # Create a Kernel object
# kernel = aiml.Kernel()

# # Load AIML files
# kernel.learn("std_startup.xml")
# kernel.respond("LOAD AIML B")

# def parse_command(user_input):
#     match = re.match(r'^python\s+-u\s+"(.+)"$', user_input)
#     if match:
#         # Extract the file path from the input
#         file_path = match.group(1)
        
#         # Execute the Python file at the specified path using subprocess
#         try:
#             subprocess.run(['python', '-u', file_path], check=True)
#         except FileNotFoundError:
#             print(f"Error: Python file '{file_path}' not found.")
#         except subprocess.CalledProcessError as e:
#             print(f"Error executing Python file: {e}")
#     else:
#         # Invalid command syntax
#         print("Invalid command syntax")

# def chat():
#     while True:
#         user_input = input("User: ")
        
#         # Check if input is a command
#         if not kernel.respond(user_input):
#             parse_command(user_input)
#         else:
#             # Process user input with AIML
#             bot_response = kernel.respond(user_input)
#             print("Bot:", bot_response)

# if __name__ == "__main__":
#     chat()