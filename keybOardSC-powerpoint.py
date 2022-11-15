import keyboard
import gui
from pythonosc.dispatcher import Dispatcher
from pythonosc import osc_server
import threading
import ctypes

# port = gui.qt()
port = gui.qt.show_get_int_dialog(None)


class run_server(threading.Thread):
    def __init__(self, name):
        threading.Thread.__init__(self)
        self.name = name

    def run(self):
        print("Serving on port:", port)
        server.serve_forever()

    def get_id(self):
        # returns id of the respective thread
        if hasattr(self, '_thread_id'):
            return self._thread_id
        for id, thread in threading._active.items():
            if thread is self:
                return id

    def raise_exception(self):
        thread_id = self.get_id()
        server.shutdown()
        res = ctypes.pythonapi.PyThreadState_SetAsyncExc(thread_id,ctypes.py_object(SystemExit))
        if res > 1:
            ctypes.pythonapi.PyThreadState_SetAsyncExc(thread_id, 0)
            print('Exception raise failure')

ip = "0.0.0.0"
# port = 50506

def tekst_handler(addr, *args):
  print(addr, args[0])
  gui.taskbar_ico(args[0])
  keyboard.write(args[0])
  keyboard.send("return")

def slide_handler(addr, args):
  print(addr, str(args))
  keyboard.write(str(args))
  keyboard.send("return")
def next_handler(addr, *args):
  print(addr)
  keyboard.send("space")
def start_handler(addr, *args):
  print(addr)
  keyboard.send("command+shift+return")
def stop_handler(addr, *args):
  print(addr)
  keyboard.send("command+shift+return")
def start_selected_handler(addr):
  print(addr)
  keyboard.send("command+return")
def presenter_handler(addr):
  print(addr)
  keyboard.send(58, True,False)
  keyboard.send("return")
  keyboard.send(58, False,True)
def key_handler(addr, args):
  print(addr, args)
  keyboard.send(args)


dispatcher = Dispatcher()
dispatcher.map("/tekst", tekst_handler)
dispatcher.map("/slide", slide_handler)
dispatcher.map("/next", next_handler)
dispatcher.map("/go", next_handler)
dispatcher.map("/start", start_handler)
dispatcher.map("/stop", stop_handler)
dispatcher.map("/esc", stop_handler)
dispatcher.map("/start/selected", start_selected_handler)
dispatcher.map("/view", presenter_handler)
dispatcher.map("/presenter", presenter_handler)
dispatcher.map("/keycombo", key_handler)

server = osc_server.ThreadingOSCUDPServer((ip, port), dispatcher)


# start app:
t1 = run_server('Thread 1')
t1.start()

gui.qt.taskbar_ico("port: "+str(port))

#  end app:
t1.raise_exception()
t1.join()

