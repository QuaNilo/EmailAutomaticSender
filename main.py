import smtplib
import csv
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import os

try:
    user_mail = input("Input your gmail > ")
    password = input("Input your app password > ")
    subject_mail = input("Input the email's title > ")
    text_file_location = str(input(" filename.txt containing email's text > "))
    while os.path.exists(text_file_location) == False:
        print(f"{text_file_location} not found")
        text_file_location = str(input(" filename.txt containing email's text > "))
    with open(text_file_location, "r") as text_file:
        data = text_file.read()

    filename = input("filename.csv containing emails and names > ")
    while os.path.exists(filename) == False:
        print(f"{filename} not found")
        filename = input("filename.csv containing emails and names > ")
    email_count = 1
    if os.path.exists(filename):
        with open(filename, "r") as csvfile:
            reader = csv.reader(csvfile)
            next(reader)
            for line in reader:
                name = line[1]
                input_content_formatted = data.format(name=name)
                if line[0] == user_mail:
                    continue
                # The mail addresses and password
                sender_address = user_mail
                sender_pass = password
                receiver_address = line[3]
                # Set up the MIME
                message = MIMEMultipart()
                message['From'] = sender_address
                message['To'] = receiver_address
                message['Subject'] = subject_mail
                # The body and the attachments for the mail
                message.attach(MIMEText(input_content_formatted, 'plain'))
                # Create SMTP session for sending the mail
                session = smtplib.SMTP('smtp.gmail.com', 587)  # use gmail with port
                session.starttls()  # enable security
                session.login(sender_address, sender_pass)  # login with mail_id and password
                text = message.as_string()
                session.sendmail(sender_address, receiver_address, text)
                session.quit()
                print(f'Mail Sent to {line[3]}')
                print(f"Emails sent {email_count}")
                email_count += 1
    else:
        print(f"{filename} not found")
    input("Press any key to leave.")
except Exception as Argument:

    # creating/opening a file
    f = open("logfile.txt", "a")

    # writing in the file
    f.write(str(Argument))

    # closing the file
    f.close()

