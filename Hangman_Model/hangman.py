import string

class HangmanAI:
    def __init__(self, wordlist_file="airlines_words.txt"):
        with open(wordlist_file, "r") as f:
            self.words = [w.strip().lower() for w in f if w.strip()]

    def suggest_letter(self, current_state, guessed_letters, guesses_remaining):
        pattern = current_state.replace(" ", "")
        candidates = []
        for word in self.words:
            if len(word) != len(pattern):
                continue
            match = True
            for wc, pc in zip(word, pattern):
                if pc != "_" and wc != pc:
                    match = False
                    break
                if pc == "_" and wc in guessed_letters:
                    match = False
                    break
            if match:
                candidates.append(word)
        freq = {}
        for word in candidates:
            for ch in word:
                if ch not in guessed_letters and ch in string.ascii_lowercase:
                    freq[ch] = freq.get(ch, 0) + 1
        if not freq:
            for ch in "etaoinshrdlcumwfgypbvkjxqz":
                if ch not in guessed_letters:
                    return ch
        return max(freq, key=freq.get)

