import requests
from bs4 import BeautifulSoup
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders
from datetime import datetime
from threading import Timer

def write_to_file(title):
 f = open("bus.txt","w+")
 write = f.write(title)
 f.close()

def email():
 user_to = 'camkim98@gmail.com'
 user_from = 'camkim98@gmail.com'

 subject = 'Routes and their service updates.'

 msg = MIMEMultipart()
 msg['From'] = user_from
 msg['To'] = user_to
 msg['Subject'] = subject

 body = 'Check out the routes.'
 msg.attach(MIMEText(body, 'plain'))

 URL = 'https://www.publictransport.com.mt/en/service-updates'

 headers = {"User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:69.0) Gecko/20100101 Firefox/69.0'}

 page = requests.get(URL, headers=headers)

 soup = BeautifulSoup(page.content, 'html.parser')

 title = str(soup.find("section", attrs={"class": "middle"}).get_text())

 write_to_file(title)

 filename = 'bus.txt'
 attachment = open(filename, 'rb')

 part = MIMEBase('application', 'octet-stream')
 part.set_payload((attachment).read())
 encoders.encode_base64(part)
 part.add_header('Content-Disposition', "attachment; filename= "+filename)

 msg.attach(part)
 text = msg.as_string()
 server = smtplib.SMTP('smtp.gmail.com', 587)
 server.ehlo()
 server.starttls()
 server.ehlo()

 server.login(user_from, 'haxwolkicdhvyrvx')

 server.sendmail(user_from, user_to, text)

 print("Email has been sent!")
 server.quit()


//was going to use this to run program automatically
#x = datetime.today()
#y = x.replace(day=x.day+1, hour=6, minute=0, second=5, microsecond=0)
#delta_t = y - x

#secs = delta_t.seconds+1

#t = Timer(secs, email)
#t.start()

email()
