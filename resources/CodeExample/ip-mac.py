def getEthName():
   #Obtiene el nombre del Ethernet
   try:
      for root, dirs, files in os.walk('/sys/class/net/'):
         for dir in dirs:
            if dir [:3] == 'enx' or dir[:3] == 'eth':
               interface = dir
   except:
      interface = 'None'
   return interface
