#import the necessary modules
#R4c0d3 @Author
import hashlib
import itertools

#Define the password hash and the dictionary
hash = "ef797c8118f02dfb649607dd5d3f8c7623048c9c063d532cc95c5ed7a898a64f"
dictionary = ["password", "abc123", "qwerty", "letmein", "monkey", "123456", "123456789", "0123456", "0123456789", "9876543210",
              "111111", "1234567890", "1234567", "quertyouip", "quertyuiop", "mynoob", "66666666", "18atcskd2w", "4<65v465",
              "google", "123qwe", "1a6v8dg7/*", "SDGsdf654+*", "zxcvbnm", "1q2w3e"]

# Iterate over all possible combinations of words in the dictionary
for guess in itertools.permutations(dictionary, 2):
    # Create a hash of the current guess
    guess_hash = hashlib.sha256("".join(guess).encode("utf-8")).hexdigest()
    # Compare the guess hash with the password hash
    if guess_hash == hash:
        # If they match, print the password and exit
        print("The password is: " + "".join(guess))
        exit()

# If the password is not in the dictionary, print a message
print("The password is not in the dictionary.")