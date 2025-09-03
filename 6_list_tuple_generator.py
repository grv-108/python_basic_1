# list and tuple generator

def getUserInput():
    """getting user input"""
    return input("Enter , separated digits : ").strip().split(",")

def main(user_input_list):
    """main function"""
    return user_input_list, tuple(user_input_list)

if __name__ == "__main__":
    print()
    user_input = getUserInput()
    user_list, user_tuple = main(user_input)
    print()
    print(f"list of user's input : {user_list}")
    print(f"tuple of user's input : {user_tuple}")