import random
class PasswordGenerator:
    def __init__(self) -> None:
        pass
    
    def generate(self):
        number_give = 11
        letter = random.randint(1,int(number_give/2))
        symbol = 0
        while True:
            symbol = random.randint(1,int(number_give/2))
            if (letter + symbol == number_give-2):
                continue
            else:
                break
        number = number_give - (letter+symbol)
        letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
        numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
        symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
        password = []
        for i in range(1,letter+1) :
            password.append(str(letters[random.randint(0,25)]))
        for i in range(1,symbol+1):
            password.append(str(symbols[random.randint(0,8)]))
        for i in range(1,number+1):
            password.append(str(numbers[random.randint(0,9)]))   
        finalpassword = ""
        capture = 0
        i = 1
        while (i<=letter+symbol+number):
            capture = random.randint(0,letter+symbol+number - 1)
            if(password[capture]=="00"):
                continue
            else:
                finalpassword += password[capture]
                password[capture] = "00"
                i+=1
        return finalpassword
    
    