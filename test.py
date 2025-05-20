import re

line = "5 + 2 ="
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
        print(f"Sending result: {result}")