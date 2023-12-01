# 1. Choose a Profile (with data saved about prefrence and life situation)
#2. Input Choices (describe with multiple choice questions)
#3. Evaluate choices based on values in profile (0-100 scale?)
from users import *



def make_descision(username):

        
    so = db.get['q_one']
    fri = db.get['q_two']
    fam = db.get['q_three']
    enj = db.get['q_four']
    imp = db.get['q_five']
   

def user_survey(user):
    ans_input1 = input("Sample Question [1-5]")
    ans_one = get_ans(ans_input1)
    user_data = db.get(user)
    user_data['q_one'].append(ans_one)
    
    ans_input2 = input("Sample Question [1-5]")
    ans_two = get_ans(ans_input2)
    user_data = db.get(user)
    user_data['q_two'].append(ans_two)

    ans_input3 = input("Sample Question [1-5]")
    ans_three = get_ans(ans_input3)
    user_data = db.get(user)
    user_data['q_three'].append(ans_three)

    ans_input4 = input("Sample Question [1-5]")
    ans_four = get_ans(ans_input4)
    user_data = db.get(user)
    user_data['q_four'].append(ans_four)

    ans_input5 = input("Sample Question [1-5]")
    ans_five = get_ans(ans_input5)
    user_data = db.get(user)
    user_data['q_five'].append(ans_five)

    home_screen(user)




def home_screen(username):
    

    while True:
        mode = input(f""" Hello {username}, I am Decisio, How Can I Help You?
                    [1] Make a Descision 
                    [2] Re-Evalute Values
                    [3] Log Out
                    [4] Close Application 
                 """)
        if mode == "1":
            make_descision(username)
        elif mode == "2":
            while True:
                warn = input("Are You Sure You Want To Re-Evalute Values (Doing So Overwrites Previous Values)? [Y/N] ")
                if warn == "Y":
                    user_survey(username)
                    break
                elif warn == "N":
                    break
                else: 
                    print("Please Input a Vaild Character [Y/N]")
        elif mode == "3":
            main()
            break
        elif mode == "4":
            break
    









def main():
    while True:
        log_reg = input("""
                    [1] Login 
                    [2] Register
                    [3] Close Application
                        """)
        if log_reg == "1":
            username = input("What is Your Username: ")
            password = input("What is Your Password: ")
            if login_user(username, password) == True:
                print("Log In Successfull")
                home_screen(username)
                break
            else:
                print("Incorrect Username or Password")
        elif log_reg == "2":
            username = input("Username:")
            password = input("Password: ")
            create_user(username, password)
            user_survey(username)
        elif log_reg == "3":
            break

            





main()





