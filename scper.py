import sys
import os
import time

dir = sys.argv[1]

files = {}

changes = int(open('changes.watcher', 'r').read())

for filename in next(os.walk(str(dir)))[2]:
    if filename != 'changes.watcher':
        files[filename] = open(filename, 'r').read()

os.system('scp ' + dir + '/* pi@raspberrypi:/media/pi/UUI1/raspberry/messages/')

while True:
    for key in files:
        if files[key] != open(key, 'r').read():
            files[key] = open(key, 'r').read()
            changes = changes + 1
            open('changes.watcher', 'w').write(str(changes))
            print('')
            print('--------------------- Change #' + str(changes) + ' ---------------------')
            os.system('scp ' + dir + '/* pi@raspberrypi:/media/pi/UUI1/raspberry/messages/')
    time.sleep(0.1)