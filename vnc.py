from Crypto.Cipher import DES

# Encrypted VNC password (8-byte hex blob)
hex_blob = "b3fc1fa2cc94950d"

# VNC static DES key
vnc_key = bytes.fromhex("a69b652e5c6db635")

# Decrypt the password
cipher = DES.new(vnc_key, DES.MODE_ECB)
decrypted = cipher.decrypt(bytes.fromhex(hex_blob))

# Print result
print("Decrypted password:", decrypted.decode('ascii', errors='ignore').strip('\x00'))
