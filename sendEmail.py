import smtplib, ssl

def send(receiver, subject, msg):

    fullmsg = 'Subject: {} \n\n{}'.format(subject, msg)

    sender = ""
    password = ""
    server = smtplib.SMTP_SSL("smtp.gmail.com", 465)
    server.login(sender, password)
    server.sendmail(sender, receiver, fullmsg)
    server.quit()