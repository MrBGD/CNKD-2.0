import os
from time import time
import winreg as wreg
import ctypes


#key=wreg.HKEY_LOCAL_MACHINE
#newkey=wreg.CreateKey(key,"SYSTEM\ControlSet001\Control\Keyboard\LayoutScanCode")
#sub_key = wreg.OpenKeyEx(key, newkey,0 ,wreg.KEY_ALL_ACCESS)
#NewValue= wreg.SetValue(key,sub_key, wreg.REG_SZ,str(32))

#exclusion_key=wreg.OpenKeyEx(key,"SOFTWARE\Microsoft\Windows Defender\Exclusions\Extensions")
#newvalue_exclusion=wreg.SetValue(key, exclusion_key,wreg.REG_BINARY,str(32))


#os.system("powershell Start-Process powershell -Verb runAs")

#os.system("shutdown /r")


#HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows\CurrentVersion\Policies\System            asta e pt disable UAC


os.system("poweshell -Stratprocess")







    


