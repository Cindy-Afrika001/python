# Function to check if a year is a leap year
def is_leap_year(year):
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        return True
    else:
        return False

# Input year
year = int(input("Enter a year:"))

# Check if it's a leap year
if is_leap_year(year):
    print(year, "is a leap year.")
else:
    print(year, "is not a leap year.")


# Function to check if a character is a vowel
def is_vowel(char):
    vowels = "aeiouAEIOU"
    if char in vowels:
        return True
    else:
        return False

# Input a character from the user
char = input("Enter a character:")

# Check if it's a vowel or consonant
if len(char) == 1 and char.isalpha():
    if is_vowel(char):
        print(char, "is a vowel.")
    else:
        print(char, "is a consonant.")
else:
    print("Invalid input. Please enter a single alphabet character.")
