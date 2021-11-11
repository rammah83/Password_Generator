import random
import string

uppers = string.ascii_uppercase
lowers = string.ascii_lowercase
digits = string.digits
specials = string.punctuation

pass_length = 6
password = []

try:
    pass_length = int(input("Enter the password length :").strip())
    least_pass = list(map(lambda x: random.choice(x), [uppers, lowers, digits]))
    if 4 <= pass_length <= 12:
        print(least_pass)
        password = least_pass + [random.choice(uppers + lowers + specials + digits * 2) for _ in range(pass_length - 3)]

    else:
        raise ValueError("Password must have at least 4 characters and no more then 12!")


except ValueError as e:
    print("Not a valid number:\n\t", e)


except Exception as e:
    print("Try again, and don't play with me!", e)

print(''.join(password))
