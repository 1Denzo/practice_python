from flask import Flask
import subprocess
import platform
from datetime import datetime, timedelta

app = Flask(__name__)

@app.route('/uptime', methods=['GET'])
def get_uptime():
    try:
        if platform.system() == "Linux":
            return uptime_linux()
        
        elif platform.system() == "Windows":
            return uptime_win()
        
        else:
            return "Unsupported operating system", 500

    except Exception as e:
        return str(e), 500
    
def uptime_linux():
    uptime_output = subprocess.check_output(['uptime', '-s']).decode('utf-8').strip()
    uptime_output = datetime.strptime(uptime_output, "%Y-%m-%d %H:%M:%S")
    uptime = datetime.now() - uptime_output 
    return f"Current uptime is {format_timedelta(uptime)}"

def uptime_win():
    uptime_output = subprocess.check_output(['wmic', 'os', 'get', 'LastBootUpTime'], stderr=subprocess.STDOUT)
    uptime_output = uptime_output.decode('utf-8').strip().split('\n')[1] 
    last_boot_time = uptime_output[:14]  
    last_boot_time = f"{last_boot_time[:4]}-{last_boot_time[4:6]}-{last_boot_time[6:8]} {last_boot_time[8:10]}:{last_boot_time[10:12]}:{last_boot_time[12:14]}"
    last_boot_time = datetime.strptime(last_boot_time, "%Y-%m-%d %H:%M:%S")
    uptime = datetime.now() - last_boot_time
    return f"Current uptime is {format_timedelta(uptime)}"
    
def format_timedelta(td: timedelta):
    total_seconds = int(td.total_seconds())
    days, remainder = divmod(total_seconds, 86400) 
    hours, remainder = divmod(remainder, 3600) 
    minutes, seconds = divmod(remainder, 60)
    return f"{days} days, {hours} hours, {minutes} minutes, {seconds} seconds"

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
