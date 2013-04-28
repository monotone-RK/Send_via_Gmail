#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
import os
import commands
import time
import smtplib
from email.MIMEText import MIMEText
from email.Header import Header
from email.Utils import formatdate

def create_message(from_addr, to_addr, subject, body, encoding):
    msg = MIMEText(body, 'plain', encoding)
    msg['Subject'] = Header(subject, encoding)
    msg['From'] = from_addr
    msg['To'] = to_addr
    msg['Date'] = formatdate()
    return msg

def send_via_gmail(from_addr, to_addr, msg):
    s = smtplib.SMTP('smtp.gmail.com', 587)
    s.ehlo()
    s.starttls()
    s.login('your_address@gmail.com', 'your_password')
    s.sendmail(from_addr, [to_addr], msg.as_string())
    s.close()

if __name__ == '__main__':
    from_addr = 'your_address@gmail.com'
    to_addr = 'to address'
    msg = create_message(from_addr, to_addr, u'subject', u'body', 'ISO-2022-JP')
    send_via_gmail(from_addr, to_addr, msg)

