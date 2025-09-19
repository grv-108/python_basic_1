# 101. URL Content Printer

# Write a Python program to access and print a URL's content to the console.
from http.client import HTTPConnection

def getUserInput():
    return input("Enter URL : ").strip()

def main():
    conn = HTTPConnection(getUserInput())
    
    conn.request("GET", "/")
    
    result = conn.getresponse()
    
    content = result.read()
    
    print(content)
    
if __name__ == "__main__":
    main()
    