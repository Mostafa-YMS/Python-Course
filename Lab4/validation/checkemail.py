import re


def chkmail(text):
    text = text.strip()
    mail = re.fullmatch(r"[^@ \t\r\n]+@[^@ \t\r\n]+\.[^@ \t\r\n]+", text)
    if len(text) != 0 and mail is not None:
        return True
    else:
        print("Email Not Valid!!")
        return False
