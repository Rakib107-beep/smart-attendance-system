from app.auth.password import hash_password, verify_password

password = "123456"

hashed_password = hash_password(password)

print("Password:", password)
print("Hash:", hashed_password)
print("Verify:", verify_password(password, hashed_password))