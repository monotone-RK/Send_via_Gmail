#!/usr/bin/env python
# -*- coding: utf-8 -*-
#******************************************************************************/
# Gmail Sender Written in Python v1.0  Last Updated 2013.04.28    monotone-RK */
#******************************************************************************/
import sys
import os
import time
import datetime
import smtplib
from optparse import OptionParser
from email.MIMEText import MIMEText
from email.Header import Header
from email.Utils import formatdate

optparser = OptionParser() 
optparser.add_option("-v","--version",action="store_true",dest="showversion",
                     default=False,help="Show the version")
optparser.add_option("-l","--loop",action="store_true",dest="loop",
                     default=False,help="Send message repeatedly")
(options, args) = optparser.parse_args()

#** smtp, port number                                                        **/
#******************************************************************************/  
SMTP = "smtp.gmail.com"
PORT = 587

#** from address, password                                                   **/
#******************************************************************************/  
FROM = "your_address@gmail.com"
PWD = "your_password"

#** to address                                                               **/
#******************************************************************************/  
TO = {"hoge":"hoge's e-mail address", 
      "foo" :"foo's e-mail address", 
      "mogu":"mogu's e-mail address"} 

#** SUBJECT                                                                  **/
#******************************************************************************/  
SUBJECT = "subject"

#** BODY                                                                     **/
#******************************************************************************/  
BODY = """
          body
              """

#** encode                                                                   **/
#******************************************************************************/  
orig_enc = "utf-8"
to_enc = "to encode"

#** functions                                                                **/
#******************************************************************************/  
def showVersion():
    print "Gmail Sender Written in Python v1.0  Last Updated 2013.04.28"

def create_message(from_addr, to_addr, subject, body, encoding):
    msg = MIMEText(body, "plain", encoding)
    msg["Subject"] = Header(subject.decode(orig_enc), encoding)
    msg["From"] = from_addr
    msg["To"] = to_addr
    msg["Date"] = formatdate(localtime=True)
    return msg

def send_via_gmail(from_addr, to_addr, msg):
    s = smtplib.SMTP(SMTP, PORT)
    s.ehlo()
    s.starttls()
    s.login(FROM, PWD)
    s.sendmail(from_addr, [to_addr], msg.as_string())
    s.close()

#** process                                                                  **/
#******************************************************************************/  
if options.showversion:
    showVersion()
    sys.exit()

if len(args) > 1:
    print "## Error! The number of argument is wrong."
    sys.exit()
elif len(args) == 1 and not options.loop:
    print "## Error! The argument is not available."
    sys.exit()

if __name__ == "__main__":
    from_addr = FROM
    print "input from_addr:", from_addr
    addrs = TO
    print "input to_addrs:"
    print "-" * 30
    for addr in sorted(addrs.keys()):
        print addr
    print "-" * 30
    print 
    print u"件名", SUBJECT
    print u"-------------------- ここから本文 --------------------"
    print BODY
    print "\n"
    print "Start to send message"
    print "=" * 30
    BODY = BODY.decode(orig_enc).encode(to_enc)    
    last_sent = 0
    send_cnt = 1
    try:
        while True:
            last_sent = 0 if last_sent == 23 and datetime.datetime.now().hour == 0 else last_sent
            if last_sent < datetime.datetime.now().hour and datetime.datetime.now().hour % 1 == 0:
                current_str = datetime.datetime.now().strftime("%Y/%m/%d %H:%M:%S")
                print "send count: %d" % send_cnt, current_str
                try:   
                    for to_addr in sorted(addrs.keys()):
                        print "select addr:", to_addr
                        msg = create_message(from_addr, addrs[to_addr], SUBJECT, BODY, to_enc)
                        send_via_gmail(from_addr, addrs[to_addr], msg)
                        print "send message to", to_addr
                        print
                    if not options.loop:
                        print "Finish to send message"
                        sys.exit()
                    last_sent = datetime.datetime.now().hour
                    send_cnt += 1
                    print "=" * 30
                except Exception as e:
                    print "*** Error ***"
                    print "type:" + str(type(e))
                    print "args:" + str(e.args)
                    print "message:" + e.message
                    print "e:" + str(e)
            time.sleep(10)
    finally:
        print "Stop sending message"
        sys.exit()
