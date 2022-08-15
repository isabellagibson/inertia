from colorama import init, Fore
import os
import time
import random
import requests

AUTORUN_APPS = [
    'https://updates.insomnia.rest/downloads/windows/latest?app=com.insomnia.app&source=website',
    'https://download.scdn.co/SpotifySetup.exe',
    'https://www.google.com/chrome/thank-you.html?statcb=0&installdataindex=empty&defaultbrowser=0#'
]

MANUALLY_INSTALLED_APPS = [
    'https://code.visualstudio.com/sha/download?build=stable&os=win32-x64-user',
    'https://github.com/git-for-windows/git/releases/download/v2.37.2.windows.2/Git-2.37.2.2-64-bit.exe',
    'https://www.dropbox.com/s/rmc4kb6b5zj7myk/OfficeSetup.exe?dl=1',
    'https://central.github.com/deployments/desktop/desktop/latest/win32',
    'https://www.win-rar.com/fileadmin/winrar-versions/winrar/winrar-x64-611.exe',
    'https://www.python.org/ftp/python/3.8.10/python-3.8.10-amd64.exe',
    'https://github.com/canton7/SyncTrayzor/releases/download/v1.1.29/SyncTrayzorSetup-x64.exe',
    'https://api2.prod.symless.com/aws-downloads/synergy/v1-core-standard/1.14.5-stable.a975f61a/synergy_1.14.5-stable.a975f61a_windows_x64.msi',
    'https://mirror.fcix.net/videolan-ftp/vlc/3.0.17.4/win64/vlc-3.0.17.4-win64.exe'
]

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

if not os.path.exists('single_click'):
    os.makedirs('single_click')

if not os.path.exists('manual_setup'):
    os.makedirs('manual_setup')

for a in AUTORUN_APPS:
    print(f'{Fore.LIGHTGREEN_EX}{a}{Fore.RESET}')
    path = f'single_click/{str(random.randint(11111,99999))}.exe'
    open(path, 'wb').write(requests.get(a).content)

time.sleep(10)

for a in MANUALLY_INSTALLED_APPS:
    print(f'{Fore.LIGHTGREEN_EX}{a}{Fore.RESET}')
    path = f'manual_setup/{str(random.randint(11111,99999))}.exe'
    open(path, 'wb').write(requests.get(a).content)
