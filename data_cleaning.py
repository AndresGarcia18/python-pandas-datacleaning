import re

def my_reversed(word: str) -> str:
    return ''.join([word[i] for i in range(-1, -len(word)-1, -1)])

def how_many(sentence: str) -> tuple[str, int, str, int]:
    vowels = 'aeiouAEIOU'
    consonants = 'bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ'
    
    count_vowels = sum(1 for char in sentence if char in vowels)
    count_consonants = sum(1 for char in sentence if char in consonants)
    
    return ("Vowels", count_vowels, "Consonants", count_consonants)

def palindrome(palindrome: str) -> bool:

    checker = False

    palindrome = palindrome.replace(" ", "").lower()
    cadena_invertida = palindrome[::-1]

    if palindrome == cadena_invertida:
        checker = True
        return checker
    else:
        return checker
    
def format_phone(phone_number: str, country: str) -> tuple[str , str]:
        
    ext_match = re.search(r'(ext\s*\d+)', phone_number, re.IGNORECASE)
    ext = ext_match.group(1) if ext_match else ""

    if ext:
        phone_number = re.sub(r'(ext\s*\d+)', '', phone_number, flags=re.IGNORECASE).strip()

    phone_number = phone_number.replace('-', '').replace(' ', '')
    phone_number = phone_number.lstrip('0')

    if len(phone_number) > 4:
        phone_number = phone_number[:4] + ' ' + phone_number[4:]

    if country.lower() == "colombia":
        phone_number = "+(57)" + phone_number
    elif country.lower() == "brazil":
        phone_number = "+(55)" + phone_number

    return (phone_number, ext)