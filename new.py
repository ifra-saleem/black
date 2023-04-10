import pandas as pd
import numpy as np
from typing import List  

class User:  
    def __init__(self, subscribed: bool):  
        self.subscribed = subscribed  
        
    def notify(self) -> None:  
        pass 


def notify_subscribed_users(users: List[User]) -> None:  
    """Notify subscribed users."""  
    subscribed_users = get_subscribed_users(users)   
    for user in subscribed_users:   
        user.notify() 

def get_subscribed_users(users: List[User]) -> List[User]:  
    """Filter subscribed users."""  
    return [user for user in users if user.subscribed]  