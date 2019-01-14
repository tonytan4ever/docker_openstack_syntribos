#!/usr/bin/env python
import argparse

from email.mime.application import MIMEApplication
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import os
import smtplib


def send_mail(smtp_server, smtp_user, smtp_password, 
              from_email='noreply@sre.att.com',
              to_email='yt658p@att.com', 
              report_file_path='output_testrun.html'):
    msg = MIMEMultipart()
    msg['From'] = from_email
    msg['To'] = to_email
    msg['Subject'] = "Syntribos Job Report"
    
    txt = MIMEText('Latest syntribos job report...')
    msg.attach(txt)
    
    filename = os.path.basename(report_file_path)
    _, file_extension = os.path.splitext(filename)
    fp = open(report_file_path, 'rb')
    attach = MIMEApplication(fp.read(),
                              _subtype=file_extension[1:])
    fp.close()
    attach.add_header('Content-Disposition','attachment',
                      filename=filename)
    msg.attach(attach)
    server = smtplib.SMTP(smtp_server)
    server.starttls()
    server.login(smtp_user, smtp_password)
    server.sendmail(msg['From'], msg['To'], msg.as_string())
    server.quit()


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("-s", "--smtp_server", type=str,
                        required=True,
                        help="Smtp Server ip/port, "
                             "e.g: smtp.office365.com:587")
    parser.add_argument("-u", "--smtp_user", type=str,
                        required=True,
                        help="smtp server login user")
    parser.add_argument("-p", "--smtp_password", type=str,
                        required=True,
                        help="smtp server login password")
    parser.add_argument("-f", "--from_email", type=str,
                        default='yt658p@att.com',
                        help="From email address")
    parser.add_argument("-t", "--to_email", type=str,
                        default='yt658p@att.com',
                        help="To email address")
    parser.add_argument("-r", "--file_path", type=str,
                        default='yt658p@att.com',
                        help="Report file path to send as an attachment")
    args = parser.parse_args()
    print("Start sending report email...")
    send_mail(
        args.smtp_server, args.smtp_user, args.smtp_password,
        from_email=args.from_email,
        to_email=args.to_email,
        report_file_path=args.file_path
    )
    print("Sending email report complete...")