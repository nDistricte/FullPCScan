import os
import subprocess
import sys
import psutil
import time
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
                        "Battlelog",
                        "PO",
                        "Phantom"]
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

# List to hold the timestamps of when 'cod.exe' was run
execution_times = []

# Get the current time
current_time = time.time()

# Define the time window (10 minutes ago)
time_window = 10 * 60  # 10 minutes in seconds

# Function to check running processes
def check_recent_cod_processes(boolean = True):
    if not boolean:
        return None
    # Iterate over all currently running processes
    for proc in psutil.process_iter(['pid', 'name', 'create_time']):
        try:
            # Filter processes by name (in this case, 'cod.exe')
            if proc.info['name'] == 'CallOfDuty.exe':
                process_start_time = proc.info['create_time']
                
                # Check if the process was started within the last 10 minutes
                if current_time - process_start_time <= time_window:
                    execution_times.append({
                        'pid': proc.info['pid'],
                        'name': proc.info['name'],
                        'create_time': time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(process_start_time))
                    })
        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
            pass


def __main__():
    print(scan(True if input("Do you want to scan for possible cheats? (Y/N): ") == "Y" else False))
    usb_events(True if input("Do you want to scan for the recent usb history? (Y/N): ") == "Y" else False)
    check_recent_cod_processes(True if input("Do you want to scan for recent cod processes? (Y/N): ") == "Y" else False)
    # Print out the recent 'cod.exe' processes
    if execution_times:
        print(f"Programs run within the last 10 minutes containing 'cod.exe':")
        for run in execution_times:
            print(f"PID: {run['pid']}, Name: {run['name']}, Started at: {run['create_time']}")
    else:
        print("No 'cod.exe' processes found in the last 10 minutes.")


        
