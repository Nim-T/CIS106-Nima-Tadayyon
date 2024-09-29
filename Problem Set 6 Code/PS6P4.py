NumOfTickets = int(input("please enter the amount of tickets you wish to purchase: "))
if NumOfTickets >= 25: TicketPrice = 50
elif NumOfTickets >= 10: TicketPrice = 60
elif NumOfTickets >=5: TicketPrice = 70
else: TicketPrice = 75
Total = NumOfTickets * TicketPrice
print("You are purchasing", NumOfTickets, "tickets at a cost of ${:,.2f}".format(TicketPrice), "per ticket")
print("Your total will be ${:,.2f}".format(Total))