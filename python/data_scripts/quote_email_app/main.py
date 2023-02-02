#send a random motivational quote via email 
import pandas
import smtplib
import random
import smtp_send_module as mail

#construct dataframe of quotes & convert to dict
quotes = pandas.read_csv("quotes.txt").to_dict()
#loop through dict of dicts {number:quote}
for key, vaule in quotes.items():
    #get a quote value from dict of dicts with random number key
    quote = quotes[key][random.randint(0, 100)]

#send email using send_email module
mail.send_email(quote)