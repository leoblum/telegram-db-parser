import os
import subprocess
import ctypes
import mmh3

TELEGRAM_IOS_REPO_PATH = '../Misc/Telegram-iOS'

command = "egrep -R -h 'class |struct ' %s" % os.path.join(TELEGRAM_IOS_REPO_PATH, 'submodules/SyncCore')
process = subprocess.run(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)

if process.stderr:
    print(process.stderr)
    exit()


items = []
for x in [x for x in process.stdout.decode().split('\n') if len(x)]:
    if ':' in x:
        x = x.split(':')[0]
    elif '{' in x:
        x = x.split('{')[0]

    if 'class ' in x:
        x = x.split('class ')[1]
    elif 'struct' in x:
        x = x.split('struct ')[1]

    items.append(x)


assert len(items) == len(set(items))

mapping = {}
for x in items:
    v = mmh3.hash(x, -137723950)
    v = str(ctypes.c_uint32(v)).split('(')[1].split(')')[0]
    mapping[x] = v
    # print('%12s %s' % (v, x))

mapping = sorted(mapping.items(), key=lambda x: x[0])
for x in mapping:
    print('%s = %s' % x)
