class MyCalendar:

    def __init__(self):
        self.storage = []

    def book(self, start: int, end: int) -> bool:
        for time in self.storage:
            if end <= time[0] or start >= time[1]:
                continue
            else:
                return False 
        self.storage.append([start,end])
        return True