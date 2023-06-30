import os
import datetime
import smtplib
from email.mime.text import MIMEText
from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

# configurando o código da automatização
os.environ['PATH'] += r"C:/chromedriver_win32"

link = "http://datalake.portodesantos.com.br/dashboard/painel-sealog"
driver = webdriver.Chrome()
driver.get(url=link)


driver.find_element(By.ID, "inputEmail").send_keys("seu_email_aqui")
driver.find_element(By.ID, "inputPassword").send_keys("sua_senha_aqui")
driver.find_element(By.CLASS_NAME, "btn").click()
sleep(2)

textToClick = "SEALOG - Últimos envios"
span_element = driver.find_element(By.XPATH, "//span[text()='" + textToClick + "']")
span_element.click()
sleep(2)

driver.find_element(By.CLASS_NAME, 'm-l-5').click()
sleep(10)

lastEventText = "ULTIMO_EVENTO"
organize_event = driver.find_element(By.XPATH, "//span[text()='" + lastEventText + "']")
organize_event.click()
sleep(1)

lastEvent = driver.find_elements(By.XPATH, "//td[@column='columns[2]']")
email = driver.find_elements(By.XPATH, "//td[@column='columns[3]']//div[@ng-if='allowHTML']")
actualData = datetime.datetime.now()

recipientEmails = []

for lastEvent, email in zip(lastEvent, email):
    lastData = datetime.datetime.strptime(lastEvent.text, "%d/%m/%y %H:%M")

    time = actualData - lastData
    hours = time.total_seconds() / 3600

    if hours > 24:
        recipientEmail = email.text.strip()
        recipientEmails.append(recipientEmail)
        print("Recipient Email:", recipientEmail)

print("Total Recipient Emails:", len(recipientEmails))

# configurando o server do email
smtp_server = "smtp.office365.com"
smtp_port = 587
smtp_username = "seu_email_aqui"
smtp_password = "sua_senha_aqui"


def send_email(recipient, subject_text, message_text):
    msg = MIMEText(message_text)
    msg["Subject"] = subject_text
    msg["From"] = smtp_username
    msg["To"] = recipient

    try:
        with smtplib.SMTP(smtp_server, smtp_port) as server:
            server.starttls()
            server.login(smtp_username, smtp_password)
            server.sendmail(smtp_username, recipient, msg.as_string())
        print(f"E-mail enviado para {recipient} com sucesso!")
    except Exception as e:
        print(f"Erro ao enviar e-mail para {recipient}: {str(e)}")


for recipientEmail in recipientEmails:
    subject = "Assunto do e-mail"
    message = "Conteúdo do e-mail"

    send_email(recipientEmail, subject, message)


sleep(2)



