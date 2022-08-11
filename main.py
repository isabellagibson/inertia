from colorama import init, Fore
import os
import time

APPLICATIONS = [
    'https://updates.insomnia.rest/downloads/windows/latest?app=com.insomnia.app&source=website']

# Get system information
os.system('cls')
print('Gathering system info, please wait...')
os_name = os.popen('systeminfo').read().split('OS Name:')[
    1].split('\n')[0].strip(' ').replace('\n', '')
install_time = os.popen('systeminfo').read().split('Original Install Date:')[
    1].split('\n')[0].strip(' ').replace('\n', '')
activation_status = os.popen(
    'powershell -command "cscript /Nologo %WINDIR%\System32\slmgr.vbs /xpr"').read().split('\n')[1].strip(' ').replace('\n', '')
os.system('cls')
sysinfo = [['Windows Edition', os_name], ['Activation Status', activation_status], ['Computer Hostname', os.path.expandvars(
    '%COMPUTERNAME%')], ['Logged-in User', os.path.expandvars('%USERNAME%')], ['Windows Install Date:', install_time]]
# Pretty-print system information
for line in sysinfo:
    a, b = line
    total = len(a) + len(b)
    ln = ((' ' * 20) + a + ' : ' +
          (' ' * (60 - (len(a) - 4) - len(b))) + b + (' ' * 20))
    print(ln)
    time.sleep(0.2)
