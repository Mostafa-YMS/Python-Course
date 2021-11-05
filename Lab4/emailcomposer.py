from validation.checkemail import chkmail


def email_composer(email, to, subject, msg, receiver_name):
    if chkmail(to):
        file = open("email", "w")
        file.write(f"From: {email}\nTo: {to}\n\nHi, {receiver_name}\n{msg}\n{subject}")
        file.close()
