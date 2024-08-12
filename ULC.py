from FlexDataCollect import FlexDataCollect
from MasterMediaDC import MasterMediaDataCollect
from NBUClient import NBUClient
from Connection import Connection
from Credentials import *
c = Connection()

def Flex():
    c.checkValidIP(HOST)
    c.connectShell(  HOST, PORT, USER, PASSWORD)
    obj1 = FlexDataCollect()
    obj1.executeCommands()


def Master():
    c.checkValidIP(HOST)
    c.connectShell(  HOST, PORT, USER, PASSWORD)
    obj1 = MasterMediaDataCollect()
    PATH = input("Enter the destination path")
    obj1.executeCommands(PATH)


def Media():
    c.checkValidIP(HOST)
    c.connectShell(  HOST, PORT, USER, PASSWORD)
    obj1 = MasterMediaDataCollect()
    PATH = input("Enter the destination path")
    obj1.executeCommands(PATH)

def nbuClient():
    c.checkValidIP(HOST)
    c.connectShell(  HOST, PORT, USER, PASSWORD)
    obj1 = NBUClient()
    PATH = input("Enter the destination path")
    obj1.executeCommands(PATH)

def default():
    return "Incorrect input"


Switcher={ 1 : Flex,
      2 : Master,
      3 : Media,
      4 : nbuClient
      }

def switch(choice):
    return Switcher.get(choice, default)()


switch(i)


