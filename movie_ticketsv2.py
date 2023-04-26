"""Movie Theatre Ticketing system - v2
Get the category and number of tickets required
created by Terry Zhen"""


# Component 1 - Welcome Screen and variable set up
def sell_ticket():
    print("********* Boobie Movies - ticketing system **********\n")

    adult_tickets = 0
    student_tickets = 0
    child_tickets = 0
    gift_tickets = 0
    total_sales = 0

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
    print(f"\nYou have now ordered {num_tickets} {ticket_type} ticket(s)")
    ticket_wanted = input("Do you wish to purchase another ticket (Y/N): "
                          "").upper()





# Main routine
sell_ticket()
