# import libraries
import datetime
import os
import random
import string

# list all possibles characters
uppers = string.ascii_uppercase
lowers = string.ascii_lowercase
digits = string.digits
specials = string.punctuation

validated_pass = None

def password_length(length:int):
    try:
        if length < 4 or length > 12 :
            raise ValueError("Password must have at least 4 characters and no more then 12!")
    except TypeError as e:
        raise TypeError("the length of password must be declared as integer, at least 4 characters and no more then 12!")


def generate_password(pass_length: int = 6, saving=False):
    """
    Return a random password of a specific length
    Parametres:
        pass_length (int): length of the password to generate.
        to_file (bool): save to a local csv file 'pass.csv'. default: False.
    Returns:
        password generated as (str)
    """

    # first check pass_length validity
    password_length(pass_length)

    global validated_pass
    password = []
    password = list(map(lambda x: random.choice(x), [uppers, lowers, digits]))
    password += [random.choice(uppers + lowers + specials + digits * 2) for _ in range(pass_length - 3)]
    validated_pass = ''.join(password)

    if saving:
        save_history(some_pass=validated_pass)
    return validated_pass


def save_history(some_pass: str = None, file_name: str = "passwords.csv"):
    """
    save password to csv file within timstamp as id
    Parametres:
        some_pass (str): a proposed password.
        file (str): the path to the file that keep password hitories. default: 'pass.csv'.
    Returns:
        None
    """
    # create directory where to save passwords if does not exist
    file_path = os.path.join(os.getcwd(), 'saved_pass')
    if not os.path.exists(file_path):
        os.mkdir(os.path.join(os.getcwd(), 'saved_pass'))
    file_path = os.path.join(file_path, file_name)

    # append generated password to saved password
    with open(file_path, encoding='utf8', mode='a') as file:
        # then check if some_pass is gived by user then use it
        if some_pass is not None:
            saved_pass = some_pass
        # check if a password is already generated then use it
        elif validated_pass is not None:
            saved_pass = validated_pass
        # then generate new password and savit
        else:
            saved_pass = generate_password()
        # apped new password, within datetime of the operation
        file.write(f"{datetime.datetime.now()},{saved_pass}\n")


if __name__ == '__main__':
    print('*' * 40, " Password Generator ", '*' * 40)
    while True:
        try:
            pass_len = int(input("Enter the password length (4 - 12) :  ").strip())
            if 4 <= pass_len <= 12:
                password_txt = generate_password(pass_len, True)
                print(f"some random password : {password_txt}")
                break
            else:
                raise ValueError("Password must have at least 4 characters and no more then 12!")

        except ValueError as e:
            print("Not a valid input, you must enter an integer at least 4 but no more then 12!")
