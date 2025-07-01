#leap year checker
print("==========LEAP YEAR CHECKER==========")
while True: 
    print("1. Start")
    print("2. Exit")
    n = input("Enter your choice:")
    if n == '1':
        year = int(input("Enter the year to be checked:"))
        if year%4 == 0:
            print(f"Yes! {year} is a Leap Year")
        else:
            print(f"No, {year} is not a Leap Year")
    
    elif n == '2':
        print("Thank you!")
        break

    else:
        print("Oh no! Invalid option selected. Let's start over..")


   