import string 
import random

def get_password_len():
    while True:
        try:
            plen = int(input("Enter password length (8-20 characters):\n"))
            if 8 <= plen <= 20:
                return plen
            else:
                print("Please enter your password between 8 and 20.")
        except ValueError:
            print("Invalid input. Please enter a valid password length.")

if __name__ == "__main__":
    s1 = string.ascii_lowercase
    # print(s1)
    
    s2 = string.ascii_uppercase
    # print(s2)
    
    s3 = string.digits
    # print(s3)
    
    s4 = string.punctuation
    # print(s4)
    
    plen = get_password_len()  # ✅ Fixed: using the correct function to handle gibberish
    
    s = []
    s.extend(list(s1))
    s.extend(list(s2))
    s.extend(list(s3))
    s.extend(list(s4))
    
    # print(s)
    random.shuffle(s)
    # print(s)
    print("Your password is: ")
    print("".join(s[0:plen]))
