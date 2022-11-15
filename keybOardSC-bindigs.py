import keyboard
import time

# ip = input("input Ip adress from this computer: ")
port = input("input port (if nothing port 50505 will be used): ")
ip = "0.0.0.0"
# port = 7070
if port == "":
  port = 50505
ip =str(ip)
port = int(port)

from pythonosc.dispatcher import Dispatcher
from pythonosc import osc_server

def tekst_handler(addr, *args):
  print(addr, args[0])
  keyboard.write(args[0])
  keyboard.send("return")

def key_handler(addr, args):
  print(addr, args)
  keyboard.send(args)


dispatcher = Dispatcher()
dispatcher.map("/tekst", tekst_handler)
dispatcher.map("/keycombo", key_handler)

server = osc_server.ThreadingOSCUDPServer((ip, port), dispatcher)
print("Serving on {}".format(server.server_address))
server.serve_forever()