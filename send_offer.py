import email, smtplib, ssl
from dotenv import load_dotenv
import os
from email import encoders
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

load_dotenv()
port = 465  # For SSL
api_email = os.environ.get("api-email")
api_pass = os.environ.get("api-pass")
email_list = os.environ.get("email-list").split(",")
context = ssl.create_default_context()
newsletter_title = "Wild times"

message = MIMEMultipart("alternative")
message["Subject"] = newsletter_title
message["From"] = api_email


text = """\
Hi,
How are you?
Real Python has many great tutorials:
www.realpython.com"""

html = """\
<html>
  <body>
    <p>Hi,<br>
       How are you?<br>
       <a href="http://www.realpython.com">Real Python</a>
       has many great tutorials.
    </p>
  </body>
</html>
"""

def create_body():
    text = ""
    html ="""\
    <html>
      <body>
    """

    html = html+ """\
      </body>
    </html>
    """
    print()

part1 = MIMEText(text, "plain")
part2 = MIMEText(html, "html")
message.attach(part1)
message.attach(part2)

try:
    with smtplib.SMTP_SSL('smtp.gmail.com', port) as server:
        server.starttls(context=context)
        server.login(api_email, api_pass)

        for i in email_list:
            message["To"] = i
            server.sendmail(
              "dggomez21@gmail.com",
              i,
              message.as_string())
except Exception as e:
    print(e)
finally:
    server.quit()