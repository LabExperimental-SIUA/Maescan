from queue import Queue
import threading
from patterns.singleton import Singleton


class QueueService(metaclass=Singleton):

    def __init__(self, p_worker_threads=2, p_task_manager=None):
        self.queue = Queue()
        self.worker_threads = p_worker_threads
        self.task_manager = p_task_manager
        for i in range(self.worker_threads):
            t = threading.Thread(target=self.start)
            t.setDaemon(True)
            t.start()

    def start(self):
        while True:
            item = [self.queue.get(block=True)]
            print("Procesando imagen: "+item[0])
            self.task_manager.process(item)
            self.queue.task_done()

    def push(self, p_image):
        if isinstance(p_image, list):
            for image in p_image:
                self.queue.put(image)
        else:
            self.queue.put(p_image)

    def is_processing(self):
        return not(self.queue.empty())

    def wait_process(self):
        print("Processing...")
        self.queue.join()

    def get_active_threads(self):
        return threading.active_count()
