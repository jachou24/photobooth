import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.image import MIMEImage
from email.mime.text import MIMEText

smtp_server = "smtp.gmail.com"  # For Gmail
port = 587  # SMTP port for TLS
sender = "jmchou@umass.edu"
appPass = "hkuv yikz hzza muqd "

def sendEmail(imgName, receiver):
  message = MIMEMultipart('related')
  message["From"] = sender
  message["To"] = receiver
  message["Subject"] = "Photobooth"
  body = "    . ݁₊ ⊹ . ݁ ⟡ ݁ . ⊹ ₊ ݁.\n~Enjoy the memories~\n    . ݁₊ ⊹ . ݁ ⟡ ݁ . ⊹ ₊ ݁.\n\nDon't forget to vote for this photobooth as your favorite project!"

  with open(imgName, 'rb') as img:
      msgImg = MIMEImage(img.read())
      message.attach(MIMEText(body, 'plain'))
      message.attach(msgImg)

  with smtplib.SMTP(smtp_server, port) as server:
      server.starttls()
      server.login(sender, appPass)
      server.send_message(message)