import os
import random
import string

def generate_ip():
    ip = '.'.join(str(random.randint(1, 254)) for _ in range(4))
    return ip

def generate_token():
    token_length = random.randint(10, 20)
    return ''.join(random.choices(string.ascii_letters + string.digits, k=token_length))

def main():
    ips = set()
    tokens = set()
    file_token = set()
    file_token = generate_token()
    file_path = os.path.join(os.path.dirname(__file__), f"{file_token}.txt")

    with open(file_path, "a+") as file:
        file.seek(0)
        existing_ips = {line.strip() for line in file}
        ips.update(existing_ips)

        if not existing_ips:
            file.write("Generated IP addresses and Tokens:\n")

        while True:
            ip = generate_ip()
            token = generate_token()

            if ip not in ips and token not in tokens:
                print(f"Hacker IP: {ip}")
                print(f"Hacker Token: {token}")
                ips.add(ip)
                tokens.add(token)
                
                file.write(f"{ip}\n")
                file.flush()  # Ensures the data is written immediately

            try:
                input_timeout = input("Press Enter to generate another IP address and Token (or type 'exit' to stop): ")
                if input_timeout.lower() == 'exit':
                    break
            except KeyboardInterrupt:
                break
    
    print(f"{len(ips)} unique IP addresses and tokens generated and saved to ips.txt.")

if __name__ == "__main__":
    main()
