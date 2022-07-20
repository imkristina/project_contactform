#string concatenation (joining strings/text)
#test "follow ________"
  #username = "True JiuJitsu" #variable - enter username to make the sentence"follow True JiuJitsu"

  #option 1
  #print('follow '+ username) #must identify username in line3

  #option 2
  #print("follow {}".format(username)) #must identify username in line3

  #option 3
  #print(f"follow {username}") **fav

name = input("Student Name: ")
appt = input("when would you like to come in? ")
phone = input("Phone Number: ")
email = input("Email:")
print()
General_Release = input("\
By hitting ENTER you hereby acknowledge and understand that any class, seminar \
or event that you or your child participates \
in will involve physical activity, close contact and learning self defense skills which involve physical \
contact. True JiuJitsu or its representatives are not liable or responsible for any risks or injuries \
as a result of participation")
print()
print()
print()


ContactForm = f"{name}, Thank you for registering for a free trial. We look forward to training \
 with you. We have you on the calendar for {appt}\
 If we have any questions or need to make changes we will reach out to you by phone at: {phone}\
 or Email: {email}."

print(ContactForm)