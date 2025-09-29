import random
import string

def generate_password(min_length,numbers=True,special_characters=True):
    letters=string.ascii_letters
    digits=string.digits
    special=string.punctuation

    characters=letters
    if numbers:
        characters+=digits
    if special_characters:
        characters+=special
    
    pwd=""
    meets_criteria=False
    has_number=False
    has_special=False

    while not meets_criteria or len(pwd)<min_length:
        new_char=random.choice(characters)
        pwd+=new_char

        if new_char in digits:
            has_number=True
        elif new_char in special:
            has_special=True
        
        meets_criteria=True
        if numbers:
            meets_criteria=has_number
        if special_characters:
            meets_criteria=meets_criteria and has_special
    return pwd

def validate_password(pwd, min_length, numbers=True, special_characters=True):
    """Check if the given password strictly meets the rules."""
    if len(pwd) < min_length:
        return False

    # Check numbers
    if numbers:
        if not any(c.isdigit() for c in pwd):
            return False
    else:
        if any(c.isdigit() for c in pwd):  # disallow digits
            return False

    # Check special characters
    if special_characters:
        if not any(c in string.punctuation for c in pwd):
            return False
    else:
        if any(c in string.punctuation for c in pwd):  # disallow specials
            return False

    return True


min_length=int(input("Enter the minimum length : "))
has_number=input("Do you want to have numbers (y/n ) ? ").lower() == "y"
has_special=input("Do you want to have special characters (y/n ) ? ").lower() == "y"

# Suggest passwords
print("\nHere are some suggested passwords:")
suggestions = [generate_password(min_length, has_number, has_special) for _ in range(5)]
for i, pwd in enumerate(suggestions, 1):
    print(f"{i}. {pwd}")

while True:
# Ask user choice
  choice = input("\nDo you want to type your own password? (y/n): ").lower()

  if choice == "y":
     user_pwd = input("Enter your password: ")
     if validate_password(user_pwd, min_length, has_number, has_special):
        print("✅ Your password is accepted:", user_pwd)
        break
     else:
        print("❌ Password does not meet the requirements! Try again !")
  else:
     selected = int(input("Enter the number of the suggested password you like (1-5): "))
     if 1 <= selected <= 5:
        print("✅ Your password is:", suggestions[selected - 1])
        break
     else:
        print("❌ Invalid choice!")