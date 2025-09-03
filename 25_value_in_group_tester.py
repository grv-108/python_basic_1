# 25. Value in Group Tester

# Write a Python program that checks whether a specified value is contained within a group of values.
# Test Data :
# 3 -> [1, 5, 8, 3] : True
# -1 -> [1, 5, 8, 3] : False


def getUserInput():
    return int(input("Enter first number you looking for in first list : ").strip()), int(input("Enter sec number look in sec list : ").strip())

def main():
    first_list = [1, 5, 8, 3]
    sec_list = [1, 5, 8, 3]
    
    first_num, sec_num = getUserInput()
    
    if first_num in first_list:
        print("True")
    else:
        print("False")
    if sec_num in sec_list:
        print("True")
    else:
        print("False")
        
if __name__ == "__main__":
    main()