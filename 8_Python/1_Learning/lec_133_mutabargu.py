def create_account(name: str, holder: str, account_holders: list = []):
    account_holders.append(holder)
    return {
        'acc_name':name,
        'main_holder':holder,
        'acc_holders':account_holders
    }


a1 = create_account('checking', 'Rolf')
a2 = create_account('checking', 'Jen')
print(a1)
print(a2)

"""
So this the mutable list argument problem because when the function (def) is initailised then it creates
the empty list. So the second time the function is called the same list is updated again. To solve this 
problem never initailize a list in the argument of a method.

"""