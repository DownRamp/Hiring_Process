# Python 3.8.0
import imaplib
import getpass
import email
import os
import sys
import traceback

from dotenv import load_dotenv

ORG_EMAIL = "@gmail.com"
FROM_EMAIL = os.environ.get("api-email")
FROM_PWD = os.environ.get("api-pass")
SMTP_SERVER = "imap.gmail.com"
SMTP_PORT = 993

# get list of current job positions
# if not on then reject with job filled

def read_email_from_gmail():
    try:
        mail = imaplib.IMAP4_SSL(SMTP_SERVER)
        mail.login(FROM_EMAIL,FROM_PWD)
        mail.select('inbox')

        data = mail.search(None, '(UNSEEN)')
        mail_ids = data[1]
        id_list = mail_ids[0].split()
        first_email_id = int(id_list[0])
        latest_email_id = int(id_list[-1])

        for i in range(latest_email_id,first_email_id, -1):
            data = mail.fetch(str(i), '(RFC822)' )
            for response_part in data:
                if response_part.get_content_maintype() == 'multipart':
                    continue
                if response_part.get('Content-Disposition') is None:
                    continue
                fileName = response_part.get_filename()
                if bool(fileName):
                    filePath = os.path.join(detach_dir, 'DataFiles', fileName)
                    if not os.path.isfile(filePath) :
                        print fileName
                        fp = open(filePath, 'wb')
                        fp.write(part.get_payload(decode=True))
                        fp.close()
                arr = response_part[0]
                if isinstance(arr, tuple):
                    msg = email.message_from_string(str(arr[1],'utf-8'))
                    email_subject = msg['subject']
                    email_from = msg['from']
                    # application-#id
                    id = email_subject.split("-")[1]


    except Exception as e:
        traceback.print_exc()
        print(str(e))

read_email_from_gmail()