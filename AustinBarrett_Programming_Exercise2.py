#Our 30 random flagged phrases
SPAM_PHRASES = ["free money",
    "cash bonus",
    "earn extra cash",
    "make money fast",
    "get paid",
    "additional income",
    "unlimited income",
    "work from home",
    "risk-free",
    "guaranteed",
    "100% free",
    "act now",
    "urgent",
    "limited time",
    "don't miss out",
    "hurry",
    "final notice",
    "time-sensitive",
    "only 24 hours",
    "you have been selected",
    "congratulations",
    "winner",
    "claim your prize",
    "prize",
    "click below",
    "click here",
    "open immediately",
    "verify your account",
    "password",
    "no obligation"
]

#Function to pull email
def get_email_message():
    #ask user to input email message
    print("Enter email message. Once finished hit ENTER to complete program: ")
    #create a list
    messages= []
    #create while loop that continues while there is a viable input
    while True:
        #user input saved into message_data variable
        message_data = input()
        #if statement that stops loop when nothing is entered
        if message_data == "":
            break
        #take the input and add it to our list
        messages.append(message_data)
    #take our separate strings and join them together to create one long message
    phrase = "\n".join(messages)
    return phrase

#A function dedicated to spam detection
def spam_detection(message,spam_phrase):
    message = message.lower()
    #our accumulator variable
    spam_score = 0
    #Dictionary to mark our spam and amount detected
    triggers_found = {}
    #for loop to count the amount of spam phrases
    for spam in spam_phrase:
        spam_count = message.count(spam)
        #if statement that adds to the accumulator variable
        if spam_count > 0:
            #take what count found in spam_count and add that too spam_score
            spam_score += spam_count
            #store the key(spam phrases) with the value(amount of times seen)
            triggers_found[spam] = spam_count

    return spam_score, triggers_found

#main function
def main():
    #pull in our get email message function so that the email message data variable contains the entire spam message
    email_message_data = get_email_message()
    #A tuple to pair spam_score=score, triggers_found=triggers
    #need to do it this way so that it's readable in the dictionary
    score,triggers = spam_detection(email_message_data,SPAM_PHRASES)

    #create spam score depending on amount found
    if score == 0:
        rating = "No Spam Detection"
    elif score <= 3:
        rating = "Low Spam Detection"
    elif score <= 7:
        rating = "Medium Spam Detection"
    else:
        rating = "High Spam Detection"

    #print results to user
    print(f"Spam Score: {score}")
    print(f"Spam Likelihood Score: {rating}")

    #print extra results found
    for phrase, count in triggers.items():
        print(f"{phrase}: {count}")
#execute code
if __name__ == "__main__":
    main()


