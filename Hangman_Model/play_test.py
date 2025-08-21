import json
from api import api_call

# Example simulation
test_input = {
    "currentWordState": "_ _ e _ a n",
    "guessedLetters": ["e", "a", "n"],
    "guessesRemaining": 4
}
print(api_call(json.dumps(test_input)))
