import itertools
import sys
import time
import threading


class Loader(threading.Thread):
    """Loader object to generate a threaded loading printout"""

    def __init__(self, message="Generating...", interval=0.1):
        super().__init__()
        self._stop_event = threading.Event()
        self.message = message
        self.interval = interval

    def run(self):
        """Run command to print loading text."""
        spinner = itertools.cycle(["-", "\\", "|", "/"])
        while not self._stop_event.is_set():
            sys.stdout.write(f"\r{self.message} {next(spinner)}")
            sys.stdout.flush()
            time.sleep(self.interval)
        sys.stdout.write("\r" + " " * (len(self.message) + 2) + "\r")
        sys.stdout.flush()

    def stop(self):
        """Flag to stop threaded Loader object."""
        self._stop_event.set()
