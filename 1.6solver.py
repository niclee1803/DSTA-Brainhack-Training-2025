from pwn import *
import re

# Connect to remote service
conn = remote("52.76.13.43", 8084)
## i want to track how many times i sent the result
count = 0
while True:
    try:
        # Receive question
        line = conn.recvuntil(b'=').decode()
        print(line)
        match = re.search(r'(\d+)\s*([+\-*])\s*(\d+)\s*=', line)
        if match:
            a = int(match.group(1))
            op = match.group(2)
            b = int(match.group(3))

            if op == '+':
                result = a + b
            elif op == '-':
                result = a - b
            elif op == '*':
                result = a * b

            conn.sendline(str(result).encode())
            print(f"Sending result: {result}")
            count += 1

    except EOFError:
        break

res = conn.recvall()
print(res.decode())
print(count)
conn.close()