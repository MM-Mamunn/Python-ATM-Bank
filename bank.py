import os
os.system('cls')
balance=0

def menu():

    print("\n ➡️  Enter your choice.\n")
    print("🔸 1.Balance check")
    print("🔸 2.Money Withdraw")
    print("🔸 3.Add money ")
    print("🔸 4. EXIT\n")

i=0
while 1:    
    os.system('cls')
    print("\n\t⏹️ BANK ⏹️\n")

    menu()
    
    menu_option=input("➡️ Enter : ")
    if menu_option=="1":
        #Balance check
        os.system('cls')
        print("🔹 Your current balance is ",balance)
        
        press_continue1=input("\n\t➡️  Enter any key to continue \n")
        
    elif menu_option=="2":

        os.system('cls')

        print(" ⏹️ Money Withdraw ⏹️")
        withdraw =int(input("\n❓ How much money do you want to withdraw :"))

        if balance == 0:
            print("\n⚠️ You don't have any money in your account!")            

        elif withdraw<500:
            print("\n⚠️ Sorry, minimun limit is 500tk")

        else:
            print(f"🔸 You have withdraw {withdraw} tk\n& you current banlace is {balance - withdraw}")           
            balance=balance-withdraw 
 
        press_continue2=input("\n\t➡️  Enter any key to continue \n")    
    
    elif menu_option=="3":
        os.system('cls')
        add_money= int(input("❓ How much money do you want to add : "))
        if add_money<500:
            print("\n⚠️ Minimum you have to add 500tk\n")

        elif add_money>50000:
            print("\n⚠️ You can not add more than 50,000tk in ATM\n")    

        else:
            balance+=add_money
            print(f"\n✅ Your balance is updated\n {add_money} tk is added to your account")

        press_continue3=input("\n\t➡️ Enter any key to continue \n")

    elif menu_option=="4":
        break               
                            

print("\nThank you\n")