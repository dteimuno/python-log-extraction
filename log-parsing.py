import re
from collections import Counter

valid_ip_pattern = r'\b(?:(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){3}' \
                   r'(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\b'

ip_counts = Counter()

with open('openssh.log', 'r') as file:
    for line in file:
        match = re.search(valid_ip_pattern, line)
        if match:
            ip = match.group(0)
            ip_counts[ip] += 1
            print(f"Found IP address: {ip}")

