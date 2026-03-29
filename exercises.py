# exercises.py
# 10 Practice Exercises — Try to solve BEFORE looking at solutions!
# Run: python exercises/exercises.py

print("=" * 50)
print("  PYTHON BEGINNER EXERCISES")
print("  Try each one before running the solution!")
print("=" * 50)

# ============================================================
# EXERCISE 1: FizzBuzz
# Print numbers 1–30. But:
# - If divisible by 3 → print "Fizz"
# - If divisible by 5 → print "Buzz"
# - If divisible by both → print "FizzBuzz"
# ============================================================
print("\n--- Exercise 1: FizzBuzz ---")
# YOUR CODE HERE ↓

# SOLUTION ↓ (delete this when practicing!)
for i in range(1, 31):
    if i % 15 == 0:
        print("FizzBuzz", end=" ")
    elif i % 3 == 0:
        print("Fizz", end=" ")
    elif i % 5 == 0:
        print("Buzz", end=" ")
    else:
        print(i, end=" ")
print()

# ============================================================
# EXERCISE 2: Reverse a string
# Input: "Python" → Output: "nohtyP"
# ============================================================
print("\n--- Exercise 2: Reverse a string ---")
# YOUR CODE HERE ↓

# SOLUTION ↓
word = "Python"
print(word[::-1])

# ============================================================
# EXERCISE 3: Count vowels in a string
# Input: "Hello World" → Output: 3
# ============================================================
print("\n--- Exercise 3: Count vowels ---")
# YOUR CODE HERE ↓

# SOLUTION ↓
text = "Hello World"
vowels = "aeiouAEIOU"
count = sum(1 for char in text if char in vowels)
print(f"Vowels in '{text}': {count}")

# ============================================================
# EXERCISE 4: Find the largest number in a list (without max())
# ============================================================
print("\n--- Exercise 4: Find largest number ---")
# YOUR CODE HERE ↓

# SOLUTION ↓
numbers = [3, 7, 1, 9, 4, 6, 8, 2]
largest = numbers[0]
for num in numbers:
    if num > largest:
        largest = num
print(f"Largest: {largest}")

# ============================================================
# EXERCISE 5: Check if a word is a palindrome
# Input: "racecar" → True, "hello" → False
# ============================================================
print("\n--- Exercise 5: Palindrome check ---")
# YOUR CODE HERE ↓

# SOLUTION ↓
def is_palindrome(word):
    word = word.lower()
    return word == word[::-1]

tests = ["racecar", "hello", "level", "world", "madam"]
for w in tests:
    print(f"'{w}' → {is_palindrome(w)}")

# ============================================================
# EXERCISE 6: Calculate factorial (without math.factorial)
# 5! = 5 × 4 × 3 × 2 × 1 = 120
# ============================================================
print("\n--- Exercise 6: Factorial ---")
# YOUR CODE HERE ↓

# SOLUTION ↓
def factorial(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

print(f"5! = {factorial(5)}")
print(f"10! = {factorial(10)}")

# ============================================================
# EXERCISE 7: Flatten a nested list
# Input: [[1,2],[3,4],[5,6]] → Output: [1,2,3,4,5,6]
# ============================================================
print("\n--- Exercise 7: Flatten list ---")
# YOUR CODE HERE ↓

# SOLUTION ↓
nested = [[1, 2], [3, 4], [5, 6]]
flat = [item for sublist in nested for item in sublist]
print(flat)

# ============================================================
# EXERCISE 8: Count word frequency in a sentence
# ============================================================
print("\n--- Exercise 8: Word frequency ---")
# YOUR CODE HERE ↓

# SOLUTION ↓
sentence = "to be or not to be that is the question"
freq = {}
for word in sentence.split():
    freq[word] = freq.get(word, 0) + 1
# Sort by frequency descending
sorted_freq = sorted(freq.items(), key=lambda x: x[1], reverse=True)
for word, count in sorted_freq:
    print(f"  '{word}': {count}")

# ============================================================
# EXERCISE 9: Simple ATM simulation
# Start with $1000. Let user deposit, withdraw, check balance.
# ============================================================
print("\n--- Exercise 9: ATM Simulation ---")
# YOUR CODE HERE ↓

# SOLUTION ↓ (simplified, non-interactive for demo)
def atm():
    balance = 1000.0
    operations = [
        ("deposit", 500),
        ("withdraw", 200),
        ("withdraw", 1500),  # Should fail
        ("balance", 0),
    ]
    for op, amount in operations:
        if op == "deposit":
            balance += amount
            print(f"Deposited ${amount}. Balance: ${balance:.2f}")
        elif op == "withdraw":
            if amount > balance:
                print(f"Insufficient funds! Balance: ${balance:.2f}")
            else:
                balance -= amount
                print(f"Withdrew ${amount}. Balance: ${balance:.2f}")
        elif op == "balance":
            print(f"Current balance: ${balance:.2f}")

atm()

# ============================================================
# EXERCISE 10: Caesar Cipher (shift letters by N positions)
# "hello" shifted by 3 → "khoor"
# ============================================================
print("\n--- Exercise 10: Caesar Cipher ---")
# YOUR CODE HERE ↓

# SOLUTION ↓
def caesar_cipher(text, shift):
    result = ""
    for char in text:
        if char.isalpha():
            base = ord('A') if char.isupper() else ord('a')
            result += chr((ord(char) - base + shift) % 26 + base)
        else:
            result += char
    return result

message = "Hello, Python!"
encrypted = caesar_cipher(message, 3)
decrypted = caesar_cipher(encrypted, -3)
print(f"Original:  {message}")
print(f"Encrypted: {encrypted}")
print(f"Decrypted: {decrypted}")

print("\n✅ All exercises complete!")
