import os

def get_uptime():
    if os.name == 'posix':
        with open('/proc/uptime', 'r') as f:
            uptime_seconds = float(f.readline().split()[0])
            uptime_string = str(int(uptime_seconds // 3600)) + " hours, " + \
                            str(int((uptime_seconds % 3600) // 60)) + " minutes"
            return uptime_string
    else:
        return "System uptime not supported on this OS."

if __name__ == "__main__":
    print("System Uptime:", get_uptime())
