import random
import time

#function for generating a random password
def generate_password():
    #set empty string for password
    password = ""

    #generate 3-5 random uppercase letters
    for i in range(random.randint(3,5)):
        temp = chr(random.randint(65,90))
        password = password + temp

    #generate 3-5 random uppercase letters
    for i in range(random.randint(3,5)):
        temp = chr(random.randint(97,122))
        password = password + temp

    #generate 3-5 random digits between 0-9
    for i in range(random.randint(3,5)):
        temp = int(random.randint(0,9))
        password = password + str(temp)

    #generate 2-4 random punctuation signs
    for i in range(random.randint(2,4)):
        temp = chr(random.randint(35,38))
        password = password + temp

    #shuffle and print password
    password = shuffle(password)
    print(password)
    return

#function for shuffling a given string
def shuffle(string):
    temp_list = list(string)
    random.shuffle(temp_list)
    return ''.join(temp_list)


if __name__ == '__main__':
    generate_password()
