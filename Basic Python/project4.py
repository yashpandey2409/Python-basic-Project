# how to send automatic emails using Python.

# first generate a google app password for your Gmail account

import os
import random
import smtplib


def automatic_email():
    user = input("Enter Your Name >>: ")
    email = input("Enter Your Email >>: ")
    message = (f"Dear {user}, Welcome to Yash.Project")
    s = smtplib.SMTP('smtp.gmail.com', 587)
    s.starttls()
    s.login("yashpandey240909@gmail.com", "csxb sasn soob axhw")
    s.sendmail('&&&&&&&&&&&', email, message)
    print("Email Sent!")
    
automatic_email()