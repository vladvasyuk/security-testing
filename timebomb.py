from threading import Timer
Timer(30, lambda : os._exit(1)).start()
