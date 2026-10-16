
import math
import secrets
import string

MIN_LENGTH = 8            
RECOMMENDED_LENGTH = 15   
MAX_LENGTH = 128          

def parse_length(raw_text):
    """
    Convert the raw text typed by the user into a valid password length.
    Raises ValueError for anything that is not a whole number inside the
    allowed range, so that a crash or an insecure password never happens.
    """
    length = int(raw_text)  
    if length < MIN_LENGTH:
        raise ValueError(f"length must be at least {MIN_LENGTH}")
    if length > MAX_LENGTH:
        raise ValueError(f"length must be at most {MAX_LENGTH}")
    return length


def ask_length():
    """Keep asking until the user gives a valid length. Returns an int."""
    while True:
        raw = input(f"Enter password length ({MIN_LENGTH}-{MAX_LENGTH}, "
                    f"{RECOMMENDED_LENGTH}+ recommended): ").strip()
        try:
            return parse_length(raw)
        except ValueError:
            print(f"Invalid length. Please enter a whole number from "
                  f"{MIN_LENGTH} to {MAX_LENGTH}.")


def ask_yes_no(question):
    """Ask a yes/no question. Returns True for yes and False for no."""
    while True:
        answer = input(question + " (y/n): ").strip().lower()
        if answer in ("y", "yes"):
            return True
        if answer in ("n", "no"):
            return False
        print("Please type y or n.")


# PHASE 2 - PROCESS (the engine): integer -> complex string
def build_pool(use_symbols):
    """Pool the available character sets using the string module."""
    pool = string.ascii_letters + string.digits
    if use_symbols:
        pool = pool + string.punctuation
    return pool


def generate_password(length, use_symbols=False):
    """
    Generate a cryptographically secure random password.

    Every character is picked with secrets.choice() from the full pool, so
    each character has exactly the same chance. The password is accepted only
    if it contains at least one letter and one number (and one symbol when
    symbols are requested); otherwise a fresh one is generated. Re-generating
    (instead of forcing certain characters into fixed spots) keeps every
    valid password equally likely, so the entropy formula stays honest.
    """
    pool = build_pool(use_symbols)

    required_sets = [string.ascii_letters, string.digits]
    if use_symbols:
        required_sets.append(string.punctuation)
    if length < len(required_sets):
        raise ValueError("length is too short for the required characters")

    while True:
        characters = [secrets.choice(pool) for _ in range(length)]
        if all(any(c in group for c in characters) for group in required_sets):
            return "".join(characters)  # one allocation, O(N)


# PHASE 3 - OUTPUT (the display): prove the strength with entropy
def calculate_entropy(length, pool_size):
    """E = L x log2(R): the unpredictability of the password in bits."""
    return length * math.log2(pool_size)


def strength_label(entropy_bits):
    """Turn the entropy number into a human readable rating."""
    if entropy_bits < 50:
        return "Weak"
    if entropy_bits < 80:
        return "Moderate"
    if entropy_bits < 100:
        return "Strong"
    return "Very strong"


def show_result(password, use_symbols):
    """Print the password and its security report."""
    pool_size = len(build_pool(use_symbols))
    entropy = calculate_entropy(len(password), pool_size)

    print("\n" + "=" * 44)
    print(f"  Password : {password}")
    print("=" * 44)
    print(f"  Length         : {len(password)} characters")
    print(f"  Character pool : {pool_size} (R)")
    print(f"  Entropy        : {entropy:.1f} bits  [E = L x log2(R)]")
    print(f"  Strength       : {strength_label(entropy)}")
    if len(password) < RECOMMENDED_LENGTH:
        print(f"  NIST 2024 note : {RECOMMENDED_LENGTH}+ characters are "
              f"recommended for high-security use.")
    print("=" * 44)


def main():
    print("=" * 44)
    print("      RANDOM PASSWORD GENERATOR")
    print("=" * 44)

    try:
        length = ask_length()
        use_symbols = ask_yes_no("Include special characters (@, #, $ ...)?")
    except (EOFError, KeyboardInterrupt):
        print("\nCancelled. No password was generated.")
        return

    password = generate_password(length, use_symbols)
    show_result(password, use_symbols)


if __name__ == "__main__":
    main()
