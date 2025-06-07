import hashlib

target_hash = "34819d7beeabb9260a5c854bc85b3e44"  # Hash of 'mypassword'
wordlist_file = "rockyou.txt"

try:
    with open(wordlist_file, "r", encoding="latin-1") as file:
        for word in file:
            word = word.strip()
            hashed_word = hashlib.md5(word.encode()).hexdigest()
            if hashed_word == target_hash:
                print("Password found:", word)
                break
        else:
            print("Password not found in the wordlist.")
except FileNotFoundError:
    print("Wordlist file not found.")
