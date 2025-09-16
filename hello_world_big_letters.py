import pyfiglet

# Prompt the user for input
user_input = input("Enter names or words: ")


# Print the entire input in big ASCII art style (horizontal)
print(pyfiglet.figlet_format(user_input))
