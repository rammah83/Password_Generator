from random_password import save_history, generate_password

while True:
    try:
        pass_len = int(input("Enter the password length (4 - 12) :  ").strip())
        password_txt = generate_password(pass_len, saving=False)
        print(f"some random password : {password_txt}")
        break

    except Exception as e:
        print("Not a valid input, you must enter an integer at least 4 but no more then 12!" )

save_history()
