from datetime import time

class StudyPlatform:
    def __init__(self, name: str, url: str, start_time: time, end_time: time):
        self.name = name
        self.url = url
        self.start_time = start_time
        self.end_time = end_time

    def is_current_time_in_range(self, current_time: time) -> bool:
        return self.start_time <= current_time <= self.end_time
