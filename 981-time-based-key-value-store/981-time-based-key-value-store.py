class TimeMap:
    def __init__(self):
        self.storage = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.storage:
            self.storage[key] = []
        self.storage[key].append([timestamp,value])

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.storage:
            return ""
        array = self.storage[key]
        if timestamp < array[0][0]:
            return ""
        pointer = len(array) - 1
        while timestamp < array[pointer][0]:
            pointer -= 1
        return array[pointer][1]
                
            


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)