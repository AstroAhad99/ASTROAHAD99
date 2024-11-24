from collections import OrderedDict, namedtuple, deque

# Ordered Dict

ord = OrderedDict()
ord['Rolf'] = 6
ord['Jose'] = 12
ord['Jen'] = 3
print(ord)

ord.move_to_end('Rolf')
ord.move_to_end('Jen', last=False)
print(ord)

ord.popitem()
print(ord)

# namedtuple gives the names to the tuple which is useful

# Normal tuple looks like
account = ('checking', 1886.20)

# Namedtuple will looks like this
Account = namedtuple('Account', ['name', 'balance'])

account_tuple = Account('checking', 1886.20)
#account_tuple = Account(*account)

print(account_tuple.name)
print(account_tuple.balance)


""" deque means double ended queue """
""" we can add or remove elements from either sides """

friends = deque(('Rolf', 'Charlie', 'Jen', 'Anne'))
friends.append('Jose') # append at the end
friends.appendleft('Anthony') # append at the front
print(friends)

friends.pop()
friends.popleft()

print(friends)