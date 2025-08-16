## Simple Rule-Based Chatbot in Python

This Python script implements a basic rule-based chatbot that interacts with users via the command line. It responds to specific user inputs with predefined responses, making it a simple example of how to create a conversational agent using conditional statements.

### How it works:

- The `chatbot()` function initializes the chatbot and starts an infinite loop to continuously accept user input.
- The chatbot greets the user and prompts for input.
- The user's input is converted to lowercase to ensure case-insensitive matching.
- Based on the user's message, the bot responds with appropriate predefined responses:
  - Greetings like "hello", "hi", or "hey"
  - Common questions like "how are you" or "what is your name"
  - Queries about weather or purpose
  - Expressions of gratitude
- If the user types "exit", the chatbot terminates the conversation with a farewell message.
- If the input doesn't match any predefined patterns, the bot responds that it didn't understand and prompts for rephrasing.

