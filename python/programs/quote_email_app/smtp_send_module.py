import smtplib


def send_email(message):
    #create object from smtplib class
    with smtplib.SMTP("smtp.gmail.com") as connection:
        email = input("Enter an e-mail address: ")
        pw = input("Enter pw: ")
        #start TLS secure connection
        connection.starttls()
        connection.login(user=email, password=pw)
        #send email method
        connection.sendmail(from_addr=email, 
        to_addrs="emirgonul@live.com", 
        msg=f"Subject:Hello\n\n{message}")