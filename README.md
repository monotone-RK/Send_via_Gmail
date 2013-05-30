Send_via_Gmail
==============
Python Script that send e-mails via Gmail. (Python 2.x, not Python 3)

People who validate 2-Step verification have to issue application-specific 
passwords. 


Setup
---------------------------------------
 1. Install python (version 2.x, more than 2.6)
 2. Input your gmail address(FROM) and password
 3. Input adresses(TO) you e-mail
 4. Set encode rule that you would like to use in Subject and Body. 
    (e.g. ISO-2022-JP handles Japanese.) 

###Usage
    python gmailsender.py [option]

    opthions:
    -h, --help     show this help message and exit
    -v, --version  Show the version
    -l, --loop     Send message repeatedly
