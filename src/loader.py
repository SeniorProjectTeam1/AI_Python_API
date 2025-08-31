import itertools
import sys
import time
import threading


class Loader(threading.Thread):
    def __init__(self, message="Generating...", interval=0.1):
        super().__init__()
        self._stop_event = threading.Event()
        self.message = message
        self.interval = interval

    def run(self):
        spinner = itertools.cycle(["-", "\\", "|", "/"])
        while not self._stop_event.is_set():
            sys.stdout.write(f"\r{self.message} {next(spinner)}")
            sys.stdout.flush()
            time.sleep(self.interval)
        sys.stdout.write("\r" + " " * (len(self.message) + 2) + "\r")
        sys.stdout.flush()

    def stop(self):
        self._stop_event.set()
