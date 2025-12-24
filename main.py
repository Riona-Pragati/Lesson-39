number=(int(input("Enter a muber to check")))

if number>50:
    print("Number is greater than 50.")
    if number%2==0:
        print("It is an even number")
    else:
        print("It is an odd number")

else:
    print("Number is less than 50")