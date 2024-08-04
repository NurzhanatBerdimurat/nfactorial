class UserManager:
    def __init__(self):
        self.users = {}
        self.next_id = 1

    def addUser(self, name):
        user_id = self.next_id
        self.users[user_id] = name
        self.next_id += 1
        return user_id

    def getUser(self, user_id):
        return self.users.get(user_id, None)

    def deleteUser(self, user_id):
        if user_id in self.users:
            del self.users[user_id]
            return True
        return False

    def findUserByName(self, name):
        return [user_id for user_id, user_name in self.users.items() if user_name == name]

def main():
    userManager = UserManager()
    
    while True:
        print("\n1. Add User")
        print("2. Get User by ID")
        print("3. Delete User by ID")
        print("4. Find Users by Name")
        print("5. Exit")
        
        choice = input("Enter your choice: ")
        
        if choice == '1':
            name = input("Enter user name: ")
            user_id = userManager.addUser(name)
            print(f"User added with ID: {user_id}")
        
        elif choice == '2':
            user_id = int(input("Enter user ID: "))
            name = userManager.getUser(user_id)
            if name:
                print(f"User name: {name}")
            else:
                print("User not found")
        
        elif choice == '3':
            user_id = int(input("Enter user ID: "))
            if userManager.deleteUser(user_id):
                print("User deleted")
            else:
                print("User not found")
        
        elif choice == '4':
            name = input("Enter user name: ")
            user_ids = userManager.findUserByName(name)
            if user_ids:
                print(f"User IDs with name {name}: {user_ids}")
            else:
                print("No users found with that name")
        
        elif choice == '5':
            break
        
        else:
            print("Invalid choice. Please try again.")

if __name__ == '__main__':
    main()