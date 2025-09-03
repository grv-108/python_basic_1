# file extension extractor

def getUserInput():
    return input("Enter filename with extension : ").strip().split(".")

if __name__ == "__main__":
    file_name, file_extension = getUserInput()
    print(f"File extension : {file_extension}")