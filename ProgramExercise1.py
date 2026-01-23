TICKET_START = 20
vacant_tickets = TICKET_START
buyer_count = 0

while vacant_tickets > 0:
    user_buy = int(input('How many tickets for purchase?: '))

    if user_buy < 1 or user_buy > 4:
        print('invalid input')
        continue

    if user_buy > vacant_tickets:
        print('Insufficient tickets')
        continue

    vacant_tickets = vacant_tickets - user_buy
    buyer_count += 1
    print('Tickets remaining: ', vacant_tickets)
    print('Total Buyers: ', buyer_count)