import json
from hangman import HangmanAI

ai = HangmanAI()

def api_call(input_json):
    data = json.loads(input_json)
    next_guess = ai.suggest_letter(
        current_state=data["currentWordState"],
        guessed_letters=data["guessedLetters"],
        guesses_remaining=data["guessesRemaining"]
    )
    return json.dumps({"nextGuess": next_guess})
