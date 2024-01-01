# Learning Chat Bot
This Python-based chat bot utilizes a knowledge base stored in a JSON file to interact with users, learn from their responses, and provide answers based on the input provided.
# Functionality
The chat bot:

Loads a knowledge base from a JSON file containing questions and answers.

Utilizes the get_close_matches() function from difflib to find the closest matching question.

Learns from user input by adding new questions and their corresponding answers to the knowledge base.

Saves the updated knowledge base back to the JSON file.
# Important Note
File Path Update:

Users are advised to update the file path within the code (load_knowledge_base() and save_knowledge_base()) to match their local directory structure and location of the knowledge base JSON file.
