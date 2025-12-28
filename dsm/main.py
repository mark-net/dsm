import subprocess
import time
import sys

servers = []

def startServer():
    proc = subprocess.Popen([sys.executable, 'server.py', '0'])
    
    time.sleep(5)
    
    if proc.poll() is None:
        servers.append(proc)
        print(f"Started server PID: {proc.pid}")
        return True
    return False

startServer()

while True:
    print(f"\nActive servers: {len(servers)}")
    print("1. Add server")
    print("2. Kill server")
    print("3. Exit")
    
    choice = input("Choose: ")
    
    if choice == '1':
        if startServer():
            print("Server added!")
        else:
            print("Failed")
    
    elif choice == '2' and servers:
        proc = servers.pop()
        proc.terminate()
        print(f"Killed {proc.pid}")
    
    elif choice == '3':
        break

for proc in servers:
    proc.terminate()
