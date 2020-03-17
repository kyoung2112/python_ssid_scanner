# Import the library
from wifi import Cell, Scheme
import re
import time
from datetime import datetime

while 1:
  # Scan using wlan0
  cells = Cell.all('wlan0')
  # Loop over the available cells
  for cell in cells:
    nowstr = datetime.now().strftime("%m/%d/%Y, %H:%M:%S.%f") 
    str = '{}: SSID {} / Quality {} / MAC {} / RSSI {} dBm' .format(nowstr, cell.ssid, cell.quality, cell.address, cell.signal)
    if re.search('marta', str, re.IGNORECASE): 
      print(str)
  time.sleep(0.075) 
