from threading import Thread
import threading
import time
import random
import signal
from datetime import datetime, timedelta


def thread_target_function(thread_ids):
    '''
    simple function to run out a random time
    :param thread_ids: list of running thread ids
    :return:
    '''
    curr_thread_id = threading.get_ident()
    thread_ids.append(curr_thread_id)
    rand_wait = random.randint(1,500)
    print(curr_thread_id, ": starting wait")
    time.sleep(rand_wait)


def thread_start(num_threads, target):
    '''
    Function to spin off n threads and appends into list to hand off to thread manager function.
    simple implementation only uses list, improved would use dict to allow for manager to keep check on each
    thread individually and only restart the problem threads.
    :param num_threads: int, number of threads to spin up
    :param target: func, name of function for threads to execute
    :return:
    '''
    threads = []
    thread_ids = []
    for i in range(num_threads):
        t = Thread(target=target, args=(thread_ids, ))
        threads.append(t)
        t.start()

    start_time = datetime.now()
    thread_manager(threads, thread_ids, start_time)


def thread_manager(threads, thread_ids, start_time):
    """
    Function to keep track of threads and restart if the restart condition is met
    as proof of concept restarts all threads after 7 minutes
    :param threads: list(Thread), list of thread objects
    :param thread_ids: list(int), list of thread ids
    :return:
    """
    while True:
        if start_time - datetime.utcnow() > timedelta(seconds=40):
            print("Restarting Threads")
            for i in range(len(thread_ids)):
                print("Killing Thread:", thread_ids[i])
                signal.pthread_kill(thread_ids[i], signal.SIGINT)
            time.sleep(1)
            for i in range(len(threads)):
                print("Reviving Thread:", thread_ids[i])
                threads[i].start()


