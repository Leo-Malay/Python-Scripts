# This is the script for the purpose of sending same mail to number of people.

# Importing the important modules.
import smtplib

# Declaring the variables
num_reiever = 0
reciever_email = []
i = 0
n = 0
email = "demoemail@demo.com"

# Asking the user for the sender's email.
user_name_sender = input("Enter your Email for login: ")
user_password_sender = input("Enter your password for login: ")

# Asking for recievers email.
while email != "":
    email = input(f"Email no.{i}: ")
    reciever_email.append(email)
    i += 1
num_reciever = len(reciever_email)

# Now asking for subject and content.
subject = input("Subject of mail: ")
content = input("Content of mail: ")
messager = f"{subject}\n\n\n{content}"

# Now logging in to the mail.
with smtplib.SMTP_SSL("smtp.gmail.com", 465) as smtp:
        smtp.login(user_name_sender, user_name_sender)
        while n < num_reiever:
            smtp.sendmail(user_name_sender, reciever_email, messager)