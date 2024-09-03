import json
from difflib import get_close_matches

# Load data from a JSON file
def load_data(file_path):
    try:
        with open(file_path, 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        print(f"Error: The file '{file_path}' was not found.")
        return None
    except json.JSONDecodeError:
        print(f"Error: Failed to decode JSON from the file '{file_path}'.")
        return None

# Function to translate a word using the loaded dictionary
def translate(word, data):
    word = word.lower()  # Convert the input word to lowercase
    if word in data:
        return data[word]
    else:
        # Find the closest match if the word is not found
        closest_matches = get_close_matches(word, data.keys(), n=1, cutoff=0.8)
        if closest_matches:
            return f"Did you mean '{closest_matches[0]}'? Definition: {data[closest_matches[0]]}"
        else:
            return None  # No match found

# Function to get the defining words from the graph
def get_defining_words(word, graph):
    word = word.lower()  # Convert the input word to lowercase
    if word in graph:
        return graph[word]
    else:
        return None  # No match found in the graph

# Main function to run the translation and graph lookup
def main():
    # Load both the dictionary and graph data
    dictionary = load_data("data.json")
    graph = load_data("graph.json")
    
    if dictionary is None or graph is None:
        return

    word = input("Enter the word you want to search: ").strip()
    
    # Get and print the word's definition
    definition = translate(word, dictionary)
    if definition:
        print(f"Definition of '{word}': {definition}")
    else:
        print(f"Error: The word '{word}' is not found in the dictionary.")

    # Get and print the defining words from the graph
    defining_words = get_defining_words(word, graph)
    if defining_words:
        print(f"Defining words for '{word}': {', '.join(defining_words)}")

# Entry point of the script
if __name__ == "__main__":
    main()
