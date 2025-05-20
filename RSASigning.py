from Crypto.Util.number import getPrime, bytes_to_long, long_to_bytes

# Generate RSA key pair (just for simulation)
p = getPrime(512)
q = getPrime(512)
n = p * q
phi = (p - 1) * (q - 1)
e = 65537
d = pow(e, -1, phi)  # modular inverse of e mod phi

# Message to sign
flag = b"CDDC2025{REDACTED}"
m = bytes_to_long(flag)

# Signature (s = m^d mod n)
s = pow(m, d, n)

print("=== Signing ===")
print(f"Public key (e, n):\n{e=}\n{n=}")
print(f"Private key d:\n{d=}")
print(f"Original message:\n{flag}")
print(f"Message as integer:\n{m=}")
print(f"Signature (s):\n{s=}")
