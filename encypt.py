import bcrypt

password = b"admin002"

#Generate salt
salt = bcrypt.gensalt()

# Hash password
hashed_password = bcrypt.hashpw(password, salt)

print(hashed_password)
 
 

#verifying password
entered_password = b"admin002"

if bcrypt.checkpw(entered_password, hashed_password):
    print("Password is correct!")
else:
    print("Wrong password!")