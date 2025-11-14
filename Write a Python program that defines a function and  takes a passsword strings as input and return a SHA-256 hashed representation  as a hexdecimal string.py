import hashlib 

def hash_Password(password):
    password_bytes = password.encode("UTF-8")
    hash_object = hashlib.sha256(password_bytes)
    password_hash = hash_object.hexdigest()
   
    return password_hash
password = input("Input your password: ")
hashed_Password = hash_Password(password)
print(f"Your hashed password is: {hashed_Password}")