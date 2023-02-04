''' Sardor Maxkamov '''
'''| 4.02.2023 |'''

days = int(input("Enter day: "))
year = days // 365
days = days % 365
month = days // 30
days = days % 30
print(f"year:{year}\ndays:{days}\nmonth:{month}")

x = input("first :")
x2 = input('second: ')
if x.find(x2) >= 0:
    print(True)
else:
    print(False)


str = "The quick brown fox jumps over the lazy og"
alphabet = "abcdefghijklmnopqrstuvwxyz"
flag=True
for char in alphabet:
    if char not in str.lower():
        flag = False
        if flag == True:
            print("Pangram")
        else:
            print("Not Pangram")