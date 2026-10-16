# Project 3: Random Password Generator (Python)

A command-line Random Password Generator built with Python. You enter a password length (for example 16), choose whether to include special characters, and the program generates a random, complex password and shows how strong it is.

Built as part of the **DecodeLabs Python Programming - Industrial Training Kit (Batch 2026)**.

## Features

- Password length from **8 to 128** characters (a warning is shown below 15, following the NIST 2024 guidance that longer is stronger)
- Letters and numbers by default (62 possible characters), with an optional **special characters** mode (94 possible characters)
- Every password contains **at least one letter and one number** (and at least one symbol when special characters are chosen)
- Shows the password **entropy in bits** and a strength rating (Weak / Moderate / Strong / Very strong)
- Invalid input (text, empty input, decimals, numbers outside the allowed range) is rejected without crashing

## Concepts used

- **Importing modules:** `secrets`, `string` and `math`
- **`string` module:** `string.ascii_letters`, `string.digits` and `string.punctuation` instead of typing the characters by hand
- **`secrets.choice()` instead of `random.choice()`:** the `random` module is predictable (it is a pseudo-random generator), while `secrets` uses the operating system's secure randomness, which is the right tool for passwords
- **`''.join(list)` instead of `password += char`:** strings cannot be changed in place, so joining a list once is faster than building the string one character at a time
- **Entropy formula:** `E = L x log2(R)`, where `L` is the password length and `R` is the size of the character pool. The result is a theoretical estimate of how unpredictable the password is
- Input validation with `try / except ValueError`
- Input -> Process -> Output structure, with the password logic kept separate from the screen (input/print) code
- `if __name__ == "__main__":` guard

## How to run

You need Python 3.6 or newer installed (the `secrets` module was added in Python 3.6).

```
python password_generator.py
```

## Example output

Your password will be different every time you run the program.

```
============================================
      RANDOM PASSWORD GENERATOR
============================================
Enter password length (8-128, 15+ recommended): 16
Include special characters (@, #, $ ...)? (y/n): y

============================================
  Password : ST:q\|)c|?V6BKT!
============================================
  Length         : 16 characters
  Character pool : 94 (R)
  Entropy        : 104.9 bits  [E = L x log2(R)]
  Strength       : Very strong
============================================
```

## Project structure

```
project3/
├── password_generator.py   # the program
└── README.md               # this file
```
