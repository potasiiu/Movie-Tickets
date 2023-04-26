"""
Movie Theatre Ticketing system - v4
Update total
created by Terry Zhen
"""


# Component 4
def confirm_order(ticket, number, cost):
    confirm = ""
    while confirm != "Y" and confirm != "N":
        confirm = input(f"\nYou have now ordered {number} {ticket_type} ticket(s)"
                        f"at a cost of ${cost * number:.2f}!"
                        f"\n'Y' or 'N': ").upper()
        if confirm == "Y":
            return True


        else:
            return False


# Component 3 -


def get_price(type):
    prices = [["A", 12.5], ["C", 7], ["S", 9], ["G", 0]]
    for price in prices:
        if price[0] == type:
            return price[1]


# Component 1 - Welcome Screen and variable set up
def sell_ticket():
    print("********* Fanfare Movies - ticketing system **********\n")

    adult_tickets = 0
    student_tickets = 0
    child_tickets = 0
    gift_tickets = 0
    total_sales = 0
    tickets_sold = 0


# Component 2 - Get the category and number of tickets required


    ticket_wanted = "Y"
    while ticket_wanted == "Y":
        ticket_type = input("What kind of ticket to you want: \n"
                            "\t'A' for Adult, or\n"
                            "\t'S' for Student or\n"
                            "\t'C' for Child, or\n"
                            "\t'G' for Gift Voucher\n"
                            ">> ").upper()
        num_tickets = int(input(f"How many {ticket_type} tickets do you want: "
                                f""))
        cost = get_price(ticket_type)

        if confirm_order(ticket_type, num_tickets, cost):
            print("Order Confirmed")
            # Componenet 5 - Update Totals
            total_sales += cost
            tickets_sold += num_tickets
            if ticket_type == "A":
                adult_tickets += num_tickets
            elif ticket_type == "S":
                student_tickets += num_tickets
            elif ticket_type == "C":
                child_tickets += num_tickets
            else:
                gift_tickets += num_tickets
        else:
            print("Order Cancelled")

        print(f"\nYou have now ordered {num_tickets} {ticket_type} ticket(s)"
              f"at a cost of ${cost * num_tickets:.2f}!")

        ticket_wanted = input("Do you wish to purchase another ticket (Y/N): "
                              "").upper()



# Main routine
sell_ticket()
