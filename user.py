class User:
    def __init__(self,user_id, username):
        self.id = user_id
        self.username = username
   
    def print_name(self):
        print(f"username:{self.username}")
    

 
user_1 = User(1,"josh")
user_1.print_name()
 