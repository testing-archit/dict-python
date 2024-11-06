import json

# Load word data from a JSON file
with open('word_data.json', 'r') as f:
    word_data = json.load(f)

def get_word_info(word):
    """
    Looks up a word in the dictionary and returns its meaning and an example sentence.
    
    Parameters:
    word (str): The word to look up
    
    Returns:
    dict: A dictionary containing the word's meaning and example sentence, or None if the word is not found
    """
    word = word.lower()  # Convert the word to lowercase to ensure case-insensitive search
    if word in word_data:
        # Extract the meaning and the example sentence
        meaning = word_data[word][0]
        example_sentence = word_data[word][1] if len(word_data[word]) > 1 else "No example sentence available."
        
        return {
            'meaning': meaning,
            'example_sentence': example_sentence,
        }
    else:
        return None

def main():
    while True:
        user_input = input("Enter a word (or 'exit' to quit): ")
        if user_input.lower() == 'exit':
            break
        
        word_info = get_word_info(user_input)
        if word_info:
            print(f"Word: {user_input}")
            print(f"Meaning: {word_info['meaning']}")
            print(f"Example Sentence: {word_info['example_sentence']}")
        else:
            print(f"Sorry, '{user_input}' is not found in the dictionary.")

if __name__ == "__main__":
    main()
