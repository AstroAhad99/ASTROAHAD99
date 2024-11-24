account = {
    'checking':1354.54,
    'saving':5647.24
}

def add_balance(amount: float, name: str = 'checking') -> float:
    account[name] += amount
    return account[name]

add_balance(500.00)

print(account['checking'])