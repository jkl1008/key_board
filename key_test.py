from pynput.keyboard import Listener,Controller,Key
import time
import threading
import webbrowser

# def on_press(key):
#     try:
#         print('alphanumeric key {0} pressed'.format(key.char))
#     except AttributeError:
#         print('special key {0} pressed'.format(key))
#
# def on_release(key):
#     print('{0} released'.format(key))
#     if key == keyboard.Key.esc:
#         return False
#
# with keyboard.Listener(on_press=on_press,on_release = on_release) as l:
#     l.join()

class ComboListener:
    def __init__(self):
        self.cur_keys = []
        self.keymap = {
            'gh':'https://github.com/',
            'wk':'https://www.wikipedia.org/'
        }
        self._run()

    def _on_press(self,key):
        try:
            self.cur_keys.append(key.char)
        except AttributeError:
            self.cur_keys.append(key.name)

    # def _on_release(self,key):
    #     if key == keyboard.Key.esc:
    #         return False
    def _cleaner(self):
            while True:
                time.sleep(0.7)
                self.cur_keys.clear()


    def get_combo(self):
        if len(self.cur_keys)>= 2:
            combo = self.cur_keys[-2:]
            return combo

    def get_parsed_combo(self):
        combo = self.get_combo()
        if combo:
            key = ''.join(combo)
            if key in self.keymap.keys():
                return self.keymap[key]

    def open_url(self):
        webbrowser.open_new_tab(self.get_parsed_combo())
        self.cur_keys.clear()

    def _run(self):
        l = Listener(on_press = self._on_press)
        l.daemon = True
        l.start()

        t = threading.Thread(target=self._cleaner)
        t.daemon = True
        t.start()

def send(content):
    for i in range(3):
        k.press(Key.backspace)
    k.type(content)




cl = ComboListener()
k = Controller()

while True:
    combo_content = cl.get_parsed_combo()
    if combo_content:
        cl.open_url()