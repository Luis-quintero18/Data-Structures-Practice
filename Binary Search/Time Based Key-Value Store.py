class TimeMap:

    def __init__(self):
        self.store = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.store:
            self.store[key] = []
        self.store[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.store:
            return ""
        
        data = self.store[key]
        low, high = 0, len(data) - 1
        best = ""

        while low <= high:
            mid = (low + high) // 2

            ts, val = data[mid]

            if ts == timestamp:
                return val
            
            elif ts < timestamp:
                best = val
                low = mid + 1
            else:
                high = mid - 1
                
        return best
        