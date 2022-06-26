from email import message
import smtplib
from email.mime.text import MIMEText #Библиотека для создания текстовых объектов (msg = MIMEtext(message))


def send_email(message, mail_theme):
    sender = "python.tryhard@gmail.com"
    password = "lmwcyzeybnuypyfh" # Можно импортировать его из переменной окружения при помощи библиотеки os (import os)
                                  # Пароль необходимо сгенерировать дополнительно в настройках безопасности
                                  # гугл аккаунта. Пароли для сторонних приложений
    server = smtplib.SMTP("smtp.gmail.com", 587) #Подключаемся к серверу
    server.starttls() #Шифрование
    
    try:
        server.login(sender, password) #Логинимся на сервере для отправки
        msg = MIMEText(message) #Сообщение
        msg["Subject"] = mail_theme
        server.sendmail(sender, sender, msg.as_string())
        return "Message was sent!"
    except Exception as _ex:
        return f'{_ex}\nCheck your login or password'

def main():
    mail_theme = input("Type theme: ")
    message = input("Type your message: ")
    print(send_email(message=message, mail_theme=mail_theme))

main()