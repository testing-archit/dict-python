import requests
from collections import defaultdict

def get_word_definition(word):
    """
    Fetch the definition of a given word using the dictionaryapi.dev API.

    Parameters:
    word (str): The word to look up.

    Returns:
    dict: A dictionary containing the word's definition information, or None if the word is not found.
    """
    try:
        url = f"https://api.dictionaryapi.dev/api/v2/entries/en/{word.lower()}"
        response = requests.get(url)
        response.raise_for_status()  # Raise an exception for non-2xx status codes
        data = response.json()

        if data:
            word_info = {
                "word": data[0]["word"],
                "phonetic": data[0].get("phonetic", "N/A"),
                "origin": data[0].get("origin", "N/A"),
                "meanings": [
                    {
                        "partOfSpeech": meaning["partOfSpeech"],
                        "definitions": [
                            {
                                "definition": definition["definition"],
                                "example": definition.get("example", "N/A"),
                                "synonyms": definition.get("synonyms", []),
                                "antonyms": definition.get("antonyms", [])
                            } for definition in meaning["definitions"]
                        ]
                    } for meaning in data[0]["meanings"]
                ]
            }
            return word_info
        else:
            return None
    except requests.exceptions.RequestException as e:
        print(f"Error fetching definition for '{word}': {e}")
        return None

def main():
    # Prompt the user to enter a word
    word = input("Enter a word: ")

    # Fetch the word definition
    word_info = get_word_definition(word)
    if word_info:
        print(f"Word: {word_info['word']}")
        print(f"Phonetic: {word_info['phonetic']}")
        print(f"Origin: {word_info['origin']}")
        print("Meanings:")
        for meaning in word_info["meanings"]:
            print(f"- Part of Speech: {meaning['partOfSpeech']}")
            for definition in meaning["definitions"]:
                print(f"  - Definition: {definition['definition']}")
                if definition["example"] != "N/A":
                    print(f"    Example: {definition['example']}")
                if definition["synonyms"]:
                    print(f"    Synonyms: {', '.join(definition['synonyms'])}")
                if definition["antonyms"]:
                    print(f"    Antonyms: {', '.join(definition['antonyms'])}")
            print()
    else:
        print(f"Sorry, '{word}' not found in the dictionary.")

if __name__ == "__main__":
    main()