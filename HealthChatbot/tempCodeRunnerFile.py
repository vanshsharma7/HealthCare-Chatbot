

    Label(root, text="Registration is successful", fg="green", font=("calibri", 14)).pack()
    Button(root,text="Click Here to proceed",command=btnSucess_Click).pack()


# Implementing event on login button

def login_verify():
    username1 = username_verify.get()
    password1 = password_verify.get()
    username_login_entry.delete(0, END)
    password_login_entry.delete(0, END)

    list_of_files = os.listdir()
    if username1 in list_of_files:
        file1 = open(username1, "r")
        verify = file1.read().splitlines()
        if password1 in verify:
            login_sucess()

        else:
            password_not_recognised()

    else:
        user_not_found()


# Designing popup for login success

def login_sucess():
    global login_success_screen
    login_success_screen = Toplevel(login_screen)
    login_success_screen.title("Success")
    login_success_screen.geometry("150x100")
    Label(login_success_screen, text="Login Success").pack()
    Button(login_success_screen, text="OK", command=delete_login_success).pack()


# Designing popup for login invalid password

def password_not_recognised():
    global password_not_recog_screen
    password_not_recog_screen = Toplevel(login_screen)
    password_not_recog_screen.title("Success")
    password_not_recog_screen.geometry("150x100")
    Label(password_not_recog_screen, text="Invalid Password ").pack()
    Button(password_not_recog_screen, text="OK", command=delete_password_not_recognised).pack()


# Designing popup for user not found

def user_not_found():
    global user_not_found_screen
    user_not_found_screen = Toplevel(login_screen)
    user_not_found_screen.title("Success")
    user_not_found_screen.geometry("150x100")
    Label(user_not_found_screen, text="User Not Found").pack()
    Button(user_not_found_screen, text="OK", command=delete_user_not_found_screen).pack()


# Deleting popups

def delete_login_success():
    login_success_screen.destroy()


def delete_password_not_recognised():
    password_not_recog_screen.destroy()


def delete_user_not_found_screen():
    user_not_found_screen.destroy()


# Designing Main(first) window

# Global variable for main_screen
main_screen = None

def main_account_screen(frmmain):
    global main_screen
    main_screen = frmmain
    main_screen.geometry("300x250")
    main_screen.title("Account Login")
    Label(main_screen, text="HealthBot", bg="yellow", width="300", height="2", font=("Calibri", 14)).pack()
    Label(main_screen, text="").pack()
    Button(main_screen, text="Login", bg="light green", height="2", width="30", command=login).pack()
    Label(main_screen, text="").pack()
    Button(main_screen, text="Register", bg="light green", height="2", width="30", command=register).pack()


    

root = Tk()
main_account_screen(root)

root.mainloop()
