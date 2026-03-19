from datetime import datetime
from collections import deque

class Patient:
    def __init__(self, name):
        self.name = name
        self.time_registered = datetime.now()

    def get_details(self):
        return f"{self.name} - {self.time_registered.strftime('%H:%M:%S')}"


class ClinicQueue:
    def __init__(self):
        self.queue = deque()
        self.total_seen = 0

    def add_patient(self, patient):
        self.queue.append(patient)

    def serve_patient(self):
        if self.queue:
            self.total_seen += 1
            return self.queue.popleft()
        return None

    def get_all_patients(self):
        return list(self.queue)

    def get_total_seen(self):
        return self.total_seen