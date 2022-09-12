from colorama import init, Fore
import os
import time
import random
import requests
import json

AUTORUN_APPS = [
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

PROGRAMS = {}
PROGRAMS = json.loads('[{"display_name": "Spotify", "aliases": ["Spotify"], "executable_url": "https://download.scdn.co/SpotifySetup.exe", "type": "autorun"}, {"display_name": "TIDAL", "aliases": ["TIDAL"], "executable_url": "https://download.tidal.com/desktop/TIDALSetup.exe", "type": "autorun"}, {"display_name": "Discord", "aliases": ["Discord"], "executable_url": "https://discord.com/api/downloads/distributions/app/installers/latest?channel=stable&platform=win&arch=x86", "type": "autorun"}, {"display_name": "Visual Studio Code", "aliases": ["Visual Studio Code", "VS Code", "VSC"], "executable_url": "https://code.visualstudio.com/sha/download?build=stable&os=win32-x64-user", "type": "manual"}, {"display_name": "Insomnia", "aliases": ["Insomnia"], "executable_url": "https://updates.insomnia.rest/downloads/windows/latest?app=com.insomnia.app&source=website", "type": "autorun"}]')

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

print('\n\nThe following applications will be installed:')
for p in PROGRAMS:
    print(' -', p['display_name'])
try:
    input('\nHit Enter to continue or CTRL+C to exit')
except:
    os.system('cls')
    exit()

if not os.path.exists('autorun'):
    os.makedirs('autorun')

for autorun in [p for p in PROGRAMS if p['type'] == 'autorun']:
    print(f'Downloading {Fore.LIGHTGREEN_EX}{autorun["display_name"]}{Fore.RESET}...')
    path = f'autorun/{str(random.randint(11111,99999))}.exe'
    open(path, 'wb').write(requests.get(a).content)