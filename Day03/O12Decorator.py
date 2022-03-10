

def bankFun(fnc):              # fnc is a variable
    def helperFun(amt):
        print("logged into the sysetem.....")
        fnc(amt)                            # call back
        print("logged out of the system......")
        print("-" * 40)

    return helperFun

@bankFun                                # decorator
def deposit(amt):
    print(f"{amt} credited into the account.....")

@bankFun
def withdraw(amt):
    print(f"{amt} debited from the account.....")

@bankFun
def transfer(amt):
    print(f"{amt} transferred from the account.....")


deposit(75000)
withdraw(15000)
transfer(8000)
