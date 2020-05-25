from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup
import smtplib 
from email.mime.multipart import MIMEMultipart 
from email.mime.text import MIMEText 
from email.mime.base import MIMEBase 
from email import encoders

myurl="https://www.newegg.com/Laptops-Notebooks/Category/ID-223?Tpk=laptops"

uClient = uReq(myurl)
page_html = uClient.read()
uClient.close()

page_soup = soup(page_html, "html.parser")

#Grabs each product
containers = page_soup.findAll("div",{"class","item-branding"})
# print(containers[0])

# titlecontainers = page_soup.findAll("a",{"class","item-title"})

# pricewas = page_soup.findAll("li",{"class","price-was"})
# print(pricewas[3].span.text)

# pricecurrent = page_soup.findAll("li",{"class","price-current"})
# # print(pricecurrent[3].strong.text)
# print(namecontainers[0].text)

# innercontainer = containers[0].findAll("div",{"class","item-branding"})
# print(innercontainer[0].a.img["title"])


filename = "latest_laptops.csv"  #The file will be created in the same directory
f = open(filename,"w")
headers = "product_name, currentprice \n"
f.write(headers)

count = 0
for container in containers:
	count += 1
# for container in containers:
# 	brand = container.a.img["title"]
# 	print(brand)

for i in range(0,count):
	titlecontainer = page_soup.findAll("a",{"class","item-title"})
	product_name = titlecontainer[i].text
	print(product_name)

	pricecurrent = page_soup.findAll("li",{"class","price-current"})
	pricecurrent_item = pricecurrent[i].strong.text
	print(pricecurrent_item)

	f.write(product_name.replace(",","|") + "," + pricecurrent_item.replace(",",".") + "\n")
	# f.write(brand+"\n")


# for titlecontainer in titlecontainers:
	# titlecontainer = page_soup.findAll("a",{"class","item-title"})
	# title = titlecontainer.text
	# print(title)
	# f.write(title + "\t" + "\n")
# for container in containers:
# 	container.findAll("div",{"class","item-branding"})
# 	for innercontainer in container:
# 		print(innercontainer)

# for pricewas_item in pricewas:
# 	wasprice = pricewas_item.span
# 	print(wasprice)

# for pricecurrent_item in pricecurrent:
# 	currentprice = pricecurrent_item.strong.text
# 	print(currentprice + "\n")
# 	f.write(currentprice + "\n")

# f.close()

#Closing the file
f.close()

# Python code to illustrate Sending mail with attachments from Gmail account
fromaddr = "senderEmail@service.com" #You might get an authentication error. You can go to https://stackoverflow.com/questions/16512592/login-credentials-not-working-with-gmail-smtp to fix the error.
toaddr = "ReceiverEmail@service.com"
password = "Enter Your Password Here"
   
# instance of MIMEMultipart 
msg = MIMEMultipart() 
  
# storing the senders email address   
msg['From'] = fromaddr 
  
# storing the receivers email address  
msg['To'] = toaddr 
  
# storing the subject  
msg['Subject'] = "Latest Laptop prices from NewEgg"
  
# string to store the body of the mail 
body = "Here are the top 12 Laptops from NewEgg"
  
# attach the body with the msg instance 
msg.attach(MIMEText(body, 'plain')) 
  
# open the file to be sent  
filename = "latest_laptops.csv" #This is just the name of the attachment file
attachment = open("latest_laptops.csv", "rb")  #The actual path to the file
  
# instance of MIMEBase and named as p 
p = MIMEBase('application', 'octet-stream') 
  
# To change the payload into encoded form 
p.set_payload((attachment).read()) 
  
# encode into base64 
encoders.encode_base64(p) 
   
p.add_header('Content-Disposition', 'attachment; filename= "%s"' % filename) 
  
# attach the instance 'p' to instance 'msg' 
msg.attach(p) 
  
# creates SMTP session 
s = smtplib.SMTP('smtp.gmail.com', 587) 
  
# start TLS for security 
s.starttls() 
  
# Authentication 
s.login(fromaddr, password) 
  
# Converts the Multipart msg into a string 
text = msg.as_string() 
  
# sending the mail 
s.sendmail(fromaddr, toaddr, text) 
  
# terminating the session 
s.quit() 