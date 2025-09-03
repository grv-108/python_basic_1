# 22. Count 4 in List

# Write a Python program to count the number 4 in a given list.

def getUserInput():
    return input("Enter values for list seperated by ',' : ").strip()

def countFour(my_list):
    my_four = 0
    for x in my_list:
        if x == 4:
            my_four += 1
    return my_four

def main():
    user_input = list(map(int, getUserInput().split(",")))
    result = countFour(user_input)
    print(result)

if __name__ == "__main__":
    main()