# Building on your solutions from the previous exercises, write a function local_greet that takes a locale as input, and returns a greeting. 
# The locale lets us greet people from different countries appropriately, even when they share a common language, 
# for example:

def greet(language_code):
    match language_code:
        case 'en':
            return 'Hi!'
        case 'fr':
            return 'Salut!'
        case 'pt':
            return 'Olá!'
        case 'de':
            return 'Hallo!'
        case 'sv':
            return 'Hej!'
        case 'af':
            return 'Haai!'

def extract_language(language_code):
    return language_code.split('_')[0]

def extract_region(locale):
    return locale[3:5]

def local_greet(locale):
    lang_code = extract_language(locale)
    reg_code = extract_region(locale)
    locale = f'{lang_code}_{reg_code}'
    match locale:
        case 'en_US':
            return 'Hey!'
        case 'en_GB':
            return 'Hello!'
        case 'en_AU':
            return 'Howdy!'
        case _:
            return greet(lang_code)
        

print(local_greet('en_US.UTF-8'))       # Hey!
print(local_greet('en_GB.UTF-8'))       # Hello!
print(local_greet('en_AU.UTF-8'))       # Howdy!

# Distinguish greetings for English speaking countries like the US, UK, Canada, or Australia in your implementation, 
# and feel free to fall back on the language-specific greetings in all other cases, 
# for example:

print(local_greet('fr_FR.UTF-8'))       # Salut!
print(local_greet('fr_CA.UTF-8'))       # Salut!
print(local_greet('fr_MA.UTF-8'))       # Salut!

# When implementing local_greet, make sure you re-use your extract_language, extract_region, and greet functions from the previous exercises.