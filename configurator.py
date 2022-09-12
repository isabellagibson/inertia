import requests
import json
import os

PROGRAMS_LIST_URL = 'https://isabellagibson.github.io/inertia/programs.json'
PROGRAMS = {}

# Get programs.json or use server-sided programs.json as a fallback
if os.path.exists('programs.json'):
    PROGRAMS = json.load(open('programs.json', 'r'))
else:
    req = requests.get(PROGRAMS_LIST_URL)
    if req.status_code == 404:
        print('Falling back to local file.')
    else:
        PROGRAMS = json.loads(req.text)

print('Injecting programs into main.py...')
tmp = open('inertia.py', 'w')
for line in open('main.py', 'r').readlines():
    ln = line.replace('\r', '').replace('\n', '')
    if ln != '# {{ PROGRAMS_LIST }}':
        tmp.write(line)
        continue
    tmp.write(f'PROGRAMS = json.loads(\'{json.dumps(PROGRAMS)}\')\n')
tmp.close()
