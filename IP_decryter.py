import os
import time
import requests
import tkinter as tk
from tkinter import filedialog

def get_ip_info(ip_address):
    try:
        url = f"https://ipinfo.io/{ip_address}/json"
        response = requests.get(url)
        if response.status_code == 200:
            return response.json()
        else:
            print(f"Failed to retrieve information for IP: {ip_address}. Status code: {response.status_code}")
            return None
    except Exception as e:
        print(f"An error occurred while fetching information for IP: {ip_address}. Error: {str(e)}")
        return None

def create_info_folder():
    folder_path = "Information_store"
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)
        print(f"Folder '{folder_path}' created.")
    else:
        print(f"Folder '{folder_path}' already exists.")

def process_ip_list(file_path):
    create_info_folder()  # Ensure the folder exists before processing
    with open(file_path, 'r') as file:
        ips = file.readlines()[1:]  # Skip the first line
        for ip in ips:
            ip = ip.strip()
            info_file_path = f"Information_store/{ip}.txt"
            if os.path.exists(info_file_path):
                print(f"Info file for {ip} already exists. Skipping...")
                continue
            print(f"Fetching information for IP: {ip}")
            info = get_ip_info(ip)
            if info is None:
                info = {'ip': ip, 'city': 'N/A', 'region': 'N/A', 'country': 'N/A', 'postal': 'N/A', 'loc': 'N/A', 'timezone': 'N/A'}
            with open(info_file_path, 'w', encoding='utf-8') as info_file:
                info_file.write("IP Information:\n")
                info_file.write(f"IP Address: {info.get('ip', 'N/A')}\n")
                info_file.write(f"City: {info.get('city', 'N/A')}\n")
                info_file.write(f"Region: {info.get('region', 'N/A')}\n")
                info_file.write(f"Country: {info.get('country', 'N/A')}\n")
                info_file.write(f"Postal Code: {info.get('postal', 'N/A')}\n")
                loc = info.get('loc', 'N/A').split(',')
                if len(loc) == 2:
                    info_file.write(f"Latitude: {loc[0]}\n")
                    info_file.write(f"Longitude: {loc[1]}\n")
                else:
                    info_file.write(f"Latitude: N/A\n")
                    info_file.write(f"Longitude: N/A\n")
                info_file.write(f"Timezone: {info.get('timezone', 'N/A')}\n")
            print(f"Info file for {ip} created successfully.")

def select_file():
    root = tk.Tk()
    root.withdraw() 
    file_path = filedialog.askopenfilename(title="Select a file", filetypes=[("Text files", "*.txt")])
    return file_path

def hacker_display(text):
    for char in text:
        print(char, end='', flush=True)
        time.sleep(0.01)
    print()

def main():
    name ="""
                                                                                                              
                                                                                                          
NNNNNNNN        NNNNNNNXXXXXXX       XXXXXXX     PPPPPPPPPPPPPPPPP  RRRRRRRRRRRRRRRRR       OOOOOOOOO     
N:::::::N       N::::::X:::::X       X:::::X     P::::::::::::::::P R::::::::::::::::R    OO:::::::::OO   
N::::::::N      N::::::X:::::X       X:::::X     P::::::PPPPPP:::::PR::::::RRRRRR:::::R OO:::::::::::::OO 
N:::::::::N     N::::::X::::::X     X::::::X     PP:::::P     P:::::RR:::::R     R:::::O:::::::OOO:::::::O
N::::::::::N    N::::::XXX:::::X   X:::::XXX       P::::P     P:::::P R::::R     R:::::O::::::O   O::::::O
N:::::::::::N   N::::::N  X:::::X X:::::X          P::::P     P:::::P R::::R     R:::::O:::::O     O:::::O
N:::::::N::::N  N::::::N   X:::::X:::::X           P::::PPPPPP:::::P  R::::RRRRRR:::::RO:::::O     O:::::O
N::::::N N::::N N::::::N    X:::::::::X            P:::::::::::::PP   R:::::::::::::RR O:::::O     O:::::O
N::::::N  N::::N:::::::N    X:::::::::X            P::::PPPPPPPPP     R::::RRRRRR:::::RO:::::O     O:::::O
N::::::N   N:::::::::::N   X:::::X:::::X           P::::P             R::::R     R:::::O:::::O     O:::::O
N::::::N    N::::::::::N  X:::::X X:::::X          P::::P             R::::R     R:::::O:::::O     O:::::O
N::::::N     N:::::::::XXX:::::X   X:::::XXX       P::::P             R::::R     R:::::O::::::O   O::::::O
N::::::N      N::::::::X::::::X     X::::::X     PP::::::PP         RR:::::R     R:::::O:::::::OOO:::::::O
N::::::N       N:::::::X:::::X       X:::::X     P::::::::P         R::::::R     R:::::ROO:::::::::::::OO 
N::::::N        N::::::X:::::X       X:::::X     P::::::::P         R::::::R     R:::::R  OO:::::::::OO   
NNNNNNNN         NNNNNNXXXXXXX       XXXXXXX     PPPPPPPPPP         RRRRRRRR     RRRRRRR    OOOOOOOOO     
                                                                                                          
                                                                                                          
                                                                                                          
                                                                                                          
                                                                                                          
                                                                                                          
                                                                                                              
        """
    green_color_code = "\033[92m"
    reset_color_code = "\033[0m"
    hacker_display(green_color_code + name + reset_color_code)
    print("Select a file containing a list of IP addresses.")
    file_path = select_file()
    if not file_path:
        hacker_display("No file selected. Exiting.")
        return
    hacker_display(f"Processing file: {file_path}")
    process_ip_list(file_path)
    hacker_display("All IP information files created successfully.")

if __name__ == "__main__":
    main()
