"""
The program we are going to do this implement reraise the error even if it is catched

If you want to run the else block in the try catch then there should not be RETURN in the try block.

If there is a FINALLY block and if return is used in EXCEPT block then still the finally block will run

"""

class User:
    def __init__(self, name, engagement):
        self.name = name
        self.engagement_metrics = engagement
    
    def __repr__(self):
        return f'User {self.name}'
    

def perform_calculation(metrics):
    return metrics['clicks'] * 5 + metrics['hits'] * 2


def send_engagement_notification(user):
    print(f'Notification sent to {user} succesfully')


def get_user_score(user_obj):
    try:
        perform_calculation(user_obj.engagement_metrics)
    except KeyError:
        print('Wrong type was passed in the function')
        #raise
    else:
        send_engagement_notification(user_obj.name)


"If you replace clicks with click it will raise the key error"

my_user = User('Rolf', {'clicks':4, 'hits':5})
get_user_score(my_user)