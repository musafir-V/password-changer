import smtplib  

from constants import list_of_users
from password_generator import random_password_generator

def email_sender(message):
    for i in list_of_users: 
        s = smtplib.SMTP('smtp.gmail.com', 587) 
        s.starttls() 
        s.login("codershiwang.awasthi@gmail.com", '1486374269512') 
        s.sendmail("sender_email_id", i, message) 
        s.quit() 
