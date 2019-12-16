from threading import Thread
import threading
from datetime import datetime, timedelta
import time
import random
import signal


def thread_target(thread_info):
    t_id = threading.get_ident()
    thread_info.append({"id": t_id, "condition": False})
    wait_time = random.randint(1, 50)
    time.sleep(wait_time)


def thread_start(num_threads, target):
    thread_info = []
    for i in range(num_threads):
        t = Thread(target=target, args=(thread_info, ))
        thread_info[i]['thread'] = t
        t.start()

    thread_management(thread_info)


def thread_management(thread_info):
    while True:
        for t in thread_info:
            if t['condition']:
                signal.pthread_kill(t['id'], signal.SIGINT)
                time.sleep(0.2)
                t['thread'].start()

