import random
import nltk
from nltk.corpus import brown

# Download and load the corpus only once
nltk.download("brown", quiet=True)
words = set(brown.words())


def generate_random_word():
    """
    - Generates a random word from the pre-loaded nltk brown corpus of English words

    Args: None

    Returns:
    - str: Randomly generated word from the English dictionary
    """
    return random.choice(list(words))  # Return a random word


if __name__ == "__main__":
    print(generate_random_word())
