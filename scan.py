import os
import subprocess
import sys

try:
    import win32evtlog  # Attempt to import the module
except ImportError:
    subprocess.check_call([sys.executable, "-m", "pip", "install", "pywin32"])
    import win32evtlog  # Try importing again after installation

starting_path = "C:"
possible_files_names = ["hack",
                        "Cod",
                        "Wz",
                        "cheat",
                        "Battlelog"]
server = 'localhost'
logtype = 'System'
hand = win32evtlog.OpenEventLog(server, logtype)

                      
def contains_file(file_name, path):
    for root, dirs, files in os.walk(path):
        if file_name in files:
            return True
    return False

def scan(boolean = True) -> list:
    if boolean:
        list_of_files = []
        for file_names in possible_files_names:
            if contains_file(file_names, starting_path):
                list_of_files.append(file_names)
        
        return list_of_files
    else:
        return None



server = 'localhost'
logtype = 'System'
hand = win32evtlog.OpenEventLog(server, logtype)

def usb_events(boolean = True):
    if not boolean:
        return None
    print("Searching for recent USB connections...")
    flags = win32evtlog.EVENTLOG_BACKWARDS_READ | win32evtlog.EVENTLOG_SEQUENTIAL_READ
    events = win32evtlog.ReadEventLog(hand, flags, 0)

    for event in events:
        if "USB" in event.StringInserts:  # Filter for USB-specific messages
            print(f"Time: {event.TimeGenerated} | Source: {event.SourceName} | Message: {event.StringInserts}")

def __main__():
    print(scan(True if input("Do you want to scan for possible cheats? (Y/N): ") == "Y" else False))
    usb_events(True if input("Do you want to scan for the recent usb history? (Y/N): ") == "Y" else False)


        
