import datetime as dt

current = dt.datetime.now()

print(f"Date : {current.strftime("%d-%m-%Y")}")
print(f"Time : {current.strftime("%H-%M-%S")}")