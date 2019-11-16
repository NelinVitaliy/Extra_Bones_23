year = int(input('Enter year: '))
if year % 4 != 0:
    print("usual year")
elif year % 100 == 0:
    if year % 400 == 0:
        print("leap-year")
    else:
        print("usual year")
else:
    print("leap-year")

#
# year = int(input())
# if year % 4 != 0 or (year % 100 == 0 and year % 400 != 0):
#     print("usual year")
# else:
#     print("intercalary year")