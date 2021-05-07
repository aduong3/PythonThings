import random

def passwordCreator():
    password = ''
    print("Welcome to the password generator!")
    name = input("What is your name? ")
    numOfupperCase = int(input("How many uppercase letters would you like? "))
    numOflowerCase = int(input("How many lowercase letters would you like? "))
    numOfDigits = int(input("How many digits letters would you like? "))
    numOfPunc = int(input("How many punctuation signs would you like? "))

    for i in range(numOfupperCase):
        upperCase = chr(random.randint(65,90))
        password += upperCase
    for i in range(numOflowerCase):
        lowerCase = chr(random.randint(97,122))
        password += lowerCase
    for i in range(numOfDigits):
        digits = chr(random.randint(48,57))
        password += digits
    for i in range(numOfPunc):
        punc = chr(random.randint(33,47))
        password += punc
    temp = list(password)
    random.shuffle(temp)
    result = ''.join(temp)
    location = input("What app/website is this password for? ")
    file1 = open("passwords.txt","a")
    file1.write(f"Name: {name} ----- App/Website: {location} ----- Password: {result}\n")
    file1.close()
    print("Please check the passwords.txt file for your information!")

def main():
    passwordCreator()

if __name__ == '__main__':
    main()