friends = [
    {
        'name':'Rolf',
        'location':'Milan'
    },
    {
        'name':'Anna',
        'location':'Milan'
    },
    {
        'name':'Jose',
        'location':'Pavia'
    }
]

your_loc = input("Enter your location: ")

friends_nearby = [friend for friend in friends if friend['location'] == your_loc]

if any(friends_nearby):
    print("You are not alone!")
else:
    print("You are alone!")