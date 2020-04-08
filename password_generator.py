# Importing libraries for random string generation

import random 
import string 

from constants import special_characters, numbers 

# Main function to generate the password randomly
# Can be provided with the length of password string 
# and also weather special characters and/or numbers 
# are needed to be the part of paasword
# for special characters only pass 
# special_character_or_number = 1
# for numbers only pass special_character_or_number = 2
# for both special character and numbers pass
# special_character_or_number = 3
# for neither special characters nor numbers pass 
# special_character_or_number anything else

def random_password_generator(length = 8, special_character_or_number = 0):
    letters = string.ascii_uppercase + string.ascii_lowercase
    
    if special_character_or_number is 1:
        letters = letters + special_characters
    
    if special_character_or_number is 2:
        letters = letters + numbers
    
    if special_character_or_number is 3:
        letters = letters + special_characters + numbers
    
    return ''.join(random.choice(letters) for i in range(length))

