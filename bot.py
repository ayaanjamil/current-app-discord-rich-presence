import psutil, win32process, win32gui, time
from pypresence import Presence


def active_window_process_name():
    pid = win32process.GetWindowThreadProcessId(
        win32gui.GetForegroundWindow())
    return psutil.Process(pid[-1]).name()


itemlist = ['discord', 'spotify', 'chrome', 'teams', 'zoom']
client_id = [ENTERTOKENHERE]
RPC = Presence(client_id)
RPC.connect()
starttime = time.time()

while True:
    try:
        x = active_window_process_name()
        x = x[:-4]
        print(x)
        if x.lower() in itemlist:
            print('works ig')
            print(RPC.update(state=f"Playing {x.capitalize()}", details="yes", large_image=f"{x.lower()}",
                             large_text="pls dont crash", start=starttime))
        time.sleep(10)
    except Exception:
        pass
