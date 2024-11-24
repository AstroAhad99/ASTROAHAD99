account = {
    'checking':1354.54, # current checking balance
    'saving':5647.24 # # current saving balance
}

transactions = [
    (-180.67, 'checking'),
    (220.00, 'checking'),
    (-234.12, 'saving'),
    (432.66, 'saving')
]

def add_balance(amount: float, name: str = 'checking') -> float:
    account[name] += amount
    return account[name]


for t in transactions:
    print(add_balance(*t)) # unpacking the tuple
    #add_balance(amount=t[0], name=t[1])
    # amount, name = t
    # add_balance(amount=amount, name=name)
