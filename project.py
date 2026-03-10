import random
import string
class passwords:
    def __init__(self,passw,login):
        self.name = passw
        self.login = login

    def generate_password():
        passw_list = []
        while passw_list != 10:
            random_choices = string.ascii_letters + string.digits + string.punctuation 
            letter = random.choice(random_choices)
            passw_list.append(letter)
        print(passw_list)
        


        #Password requirments : 10 characters, minimum 2 punctuation signs, minimum 3 digits

    


    def save_on_pc():
        pass
        #use I/O


    def check_validaty():
        pass
        #use regular expressions


class login:
    pass
#same in here






n = generate_password()