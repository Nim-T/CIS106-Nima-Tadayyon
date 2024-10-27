def OutOfDoorPrice(MSRP,Make,Model,EV):
    if Make.upper() == "HONDA" and Model.upper() == "ACCORD":
        PercentageOff = 0.1
    elif Make.upper() == "TOYOTA" and Model.upper() == "RAV4" or Model.upper() == "RAV-4":
        PercentageOff = 0.15
    elif EV == "Y":
        PercentageOff = 0.3
    else:
        PercentageOff = 0.05
    NewMSRP = MSRP * (1 - PercentageOff)
    ActualPrice = NewMSRP * 1.07
    return ActualPrice

def Main():
    sumMSRP = 0
    sumActual = 0
    run = input("Do you want to run this progam? (Y/N): ")
    while run.upper() == "Y":
        Make = input("Enter vehicle make: ")
        Model = input("Enter vehicle model: ")
        MSRP = float(input("Enter vehicle MSRP: "))
        EV = input("Is the vehicle an EV? (Y/N): ")
        ActualPrice = OutOfDoorPrice(MSRP,Make,Model,EV)
        sumMSRP = sumMSRP + MSRP
        sumActual = sumActual + ActualPrice
        print("Total after discount + tax is: ${:,.2f}".format(ActualPrice))
        run = input("\nDo you want to run this progam again? (Y/N): ")
    else:
        print("=======================")
        print("Sum of all MSRPs entered: ${:,.2f}".format(sumMSRP))
        print("Sum of all totals: ${:,.2f}".format(sumActual))
        print("\n Thank you for using this program!")

Main()