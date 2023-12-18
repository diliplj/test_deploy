from random import randint
from rest_form import settings
import smtplib

def six_digit_otp(digits,email=None):
    range_start = 10**(digits-1)
    range_end = (10**digits)-1
    return randint(range_start, range_end) , email


def send_otp_to_email(otp_number, email=None):
    msg = ""
    print("email ",email)
    SUBJECT = "Received OTP from Kp revilrazor "
    msg = "Hi welcome to Karthick's BLOG \n \n \n Your OTP is "+ str(otp_number)+" {0}".format(SUBJECT)	
    MAIL_SEND_TO = email
    s = smtplib.SMTP(settings.EMAIL_HOST, settings.EMAIL_PORT)
    s.starttls()
    s.login(settings.MY_MAIL, settings.EMAIL_HOST_PASSWORD)
    s.sendmail(settings.MY_MAIL,MAIL_SEND_TO,msg)
    s.quit()
    msg=True
    return msg