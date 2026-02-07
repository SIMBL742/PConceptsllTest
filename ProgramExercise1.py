#Set initial ticket amount
TICKET_START = 10
#Link vacant_tickets to initial ticket amount
vacant_tickets = TICKET_START
#create variable for buyer counter
buyer_count = 0

#If statements wrapped in a while loop to create strict purchase rules
while vacant_tickets > 0:
    #variable to monitor int of tickers from each buyer
    user_buy = int(input('Hello Park Attendee! How many tickets for purchase today?: '))

    #If statement to keep ticket purchase between 1 and 4
    if user_buy < 1 or user_buy > 4:
        print('invalid input')
        continue

    #If statement to create failsafe for insufficient tickets
    if user_buy > vacant_tickets:
        print('Insufficient tickets')
        continue

    #deduct tickets bought from ticket counter
    vacant_tickets = vacant_tickets - user_buy
    #add to buyer count every purchase
    buyer_count += 1
    #print tickets remaining and buyer count
    print('Tickets remaining: ', vacant_tickets)
    print('Total Buyers: ', buyer_count)