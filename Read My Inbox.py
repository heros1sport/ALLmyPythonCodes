# no need to import smtplib for this code
# no need to import time for this code
import imaplib
import email


def read_email_from_gmail():
        mail = imaplib.IMAP4_SSL('imap.gmail.com')
        mail.login('r21907shaurya@dpsrkp.net','ZZ1dfg2')
        mail.select('inbox')

        result, data = mail.search(None, 'ALL')
        mail_ids = data[0]

        id_list = mail_ids.split()   
        first_email_id = int(id_list[0])
        latest_email_id = int(id_list[-1])

        for i in range(latest_email_id,first_email_id, -1):
            # need str(i)
            result, data = mail.fetch(str(i), '(RFC822)' )

            for response_part in data:
                if isinstance(response_part, tuple):
                    # from_bytes, not from_string
                    msg = email.message_from_bytes(response_part[1])
                    email_subject = msg['subject']
                    email_from = msg['from']
                    print('From : ' + email_from + '\n')
                    print('Subject : ' + email_subject + '\n')

# nothing to print here
read_email_from_gmail()
