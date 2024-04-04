# Import the random library to choose greetings randomly
import random

# Define greetings list containing common greetings
greetings = ["hi", "hello", "hey"]

# Define responses list corresponding to the greetings
responses = ["Hi there!", "Glad you're here!", "What can I do for you today?"]

# Create a knowledge base dictionary to store information for specific keywords
knowledge_base = {
    "weather": "I can't access real-time weather information, but I can tell you some fun facts. Did you know...",
    "time": "Unfortunately, I cannot access the current time directly. However, you can check your device's clock.",
    "joke": "Why did the scarecrow win an award? Because he was outstanding in his field!",
}

# Define a function `chat(message)` to process user input and respond
def chat(message):
  """
  This function takes a user message, processes it, and returns a response.

  Args:
      message (str): The user's input message.

  Returns:
      str: The chatbot's response to the user's message.
  """

  # Convert the message to lowercase for case-insensitive matching
  message = message.lower()

  # Check if any word in the message matches a greeting
  if any(word in message for word in greetings):
    # Choose a random response from the greetings list
    return random.choice(responses)

  # Check if the entire message matches a keyword in the knowledge base
  elif message in knowledge_base:
    # Return the corresponding information or predefined response from the knowledge base
    return knowledge_base[message]

  # If no match is found, provide a generic fallback response
  else:
    return "I am still learning, but I am always happy to chat! Tell me more about yourself."

# Continuously loop to interact with the user
while True:
  # Prompt the user for input
  user_input = input("You: ")
  # Print the user's input for clarity
  print(user_input)

  # Get the chatbot's response to the user's input
  response = chat(user_input)

  # Print the chatbot's response prefixed with "Chatbot:"
  print("Chatbot:", response)
