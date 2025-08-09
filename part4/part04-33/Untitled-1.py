def email_checker(email):
    find_at = email.find("@")
    if email[:find_at].isalpha() == False:
        return False
    find_dot = email.find(".")
    if email[find_at + 1:find_dot].isalpha() == False:
        return False
    if email[find_dot + 1:].isalpha() == False:
        return False
    return True
    
    
    
    





print(email_checker("buzi@homi.com"))