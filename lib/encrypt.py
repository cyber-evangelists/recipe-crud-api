import bcrypt

def encrypt(password):
    
    salt = b''

    password_bytes = password.encode('utf-8')
    
    hash = bcrypt.hashpw(password_bytes, salt)
    return hash
    

