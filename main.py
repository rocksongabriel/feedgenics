import os
import re
import smtplib
import time
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from string import Template

import feedparser
from schedule import every, repeat, run_pending
from twilio.rest import Client

from dotenv import load_dotenv

load_dotenv()

# Set up SMTP server
session = smtplib.SMTP("smtp.gmail.com", 587)
session.starttls()
from_address = os.environ.get("EMAIL_ADDRESS")
password = os.environ.get("EMAIL_PASSWORD")

def remove_tags(text):
    # function to remove the tags from the summary
    TAG_RE = re.compile(r"<[^>]+>")
    return TAG_RE.sub("", text)


# function to read a file
def read_template(filename):
    with open(filename, "r", encoding="utf-8") as template_file:
        template_file_content = template_file.read()
    return Template(template_file_content)


# account_sid = os.environ.get("SID")
account_sid = os.environ.get("ACCOUNT_SID")
auth_token = os.environ.get("AUTH_TOKEN")


# function to send sms using twilio
def send_sms(entry):
    from_phone = "+19034209352"
    to_phone = "+233551528489"

    client = Client(account_sid, auth_token)

    message = client.messages.create(
        body=f"{entry.title} - {entry.link}", from_=from_phone, to=to_phone
    )

    print(message.sid)


# function to send an email
def send_email(entry):
    session.login(from_address, password)
    
    message_template = read_template("templates/email.txt")
    to_address = "thegabrielrockson@gmail.com"

    msg = MIMEMultipart()  # create a message
    message = message_template.substitute(
        TITLE=entry.title, LINK=entry.link, SUMMARY=remove_tags(entry.summary)
    )

    # Setup the parameters of the message
    msg["From"] = from_address
    msg["To"] = to_address
    msg["Subject"] = f"Most Recent Upwork Entry - {entry.title}"

    # Add in the message body
    msg.attach(MIMEText(message, "plain"))

    # Send the message via the server
    session.send_message(msg)

    print("Email sent")


@repeat(every(10).minutes)
def check_most_recent_feed():
    most_recent__url = "https://www.upwork.com/ab/feed/topics/rss?securityToken=2f5d5ccd155d0ed6da9d7645a7a421fd418dfbd3d61b4c516bf0367377c57f619ebc1852950b1f1d78e111c66f552da4eb3297b0beefa4d1c9b9d4b97883aac8&userUid=1492101406951632896&orgUid=1492101406951632897&topic=most-recent"
    rss = feedparser.parse(most_recent__url)

    # TODO - send the last 3 most recent

    entry = rss.entries[0]

    send_email(entry)
    send_sms(entry)


def main():
    while True:
        print("-------------- application running ---------------")
        run_pending()
        time.sleep(1)


if __name__ == "__main__":
    main()

# TODO
# todo - create a very simple csv file and append the just recent update to it, and if the current one and the new one are
# todo - not the same, send the mail

# TODO - add error handling to the code