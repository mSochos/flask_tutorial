import time
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
from shutil import copyfile


class Watcher:
    DIRECTORY_TO_WATCH = "/Users/Manos/Documents/development/ides_workspaces/atom/flask_tutorial"

    def __init__(self):
        self.observer = Observer()

    def run(self):
        event_handler = Handler()
        self.observer.schedule(event_handler, self.DIRECTORY_TO_WATCH, recursive=True)
        self.observer.start()
        try:
            while True:
                time.sleep(5)
        except:
            self.observer.stop()
            print ('Error')

        self.observer.join()


class Handler(FileSystemEventHandler):

    @staticmethod
    def on_any_event(event):
        if event.is_directory:
            return None

        elif event.event_type == 'created':
            if 'header' in event.src_path :
                return
            # Take any action here when a file is first created.
            print ("Received created event - %s." + event.src_path)
            print ("Creating file and Adding header" + event.src_path)
            src = event.src_path
            dst = 'cbe_logs' + '_header'
            copyfile(src, dst)
            with open(dst, 'r+') as f:
                content = f.read()
                f.seek(0, 0)
                f.write('RID,decision,decisionDate,error,isPilot,errorMessage,shipmentNumber,vesselVoyages'+ '\n' + content)

        elif event.event_type == 'modified':
            # Taken any action here when a file is modified.
            print ("Dropping...Received modified event - %s." + event.src_path)

if __name__ == '__main__':
    w = Watcher()
    w.run()
