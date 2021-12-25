def progressBar(current, total, barLength = 20):
    percent = float(current) * 100 / total
    arrow   = '-' * int(percent/100 * barLength - 1) + '>'
    spaces  = ' ' * (barLength - len(arrow))

    print('Progress: [%s%s] %d %%' % (arrow, spaces, percent), end='\r')

i=1
import time

progressBar(i,100)

while i < 100:
    i = i + 1
    time.sleep(1)
    progressBar(i, 100)

