class TimeMap:

    def __init__(self):
        self.table = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key in self.table:
            self.table[key].append((timestamp, value))
        else:
            self.table[key] = [(timestamp, value)]    
    
    def get(self, key: str, timestamp: int) -> str:
        search = self.table.get(key, [])
        l, r = 0, len(search)
        while l < r:
            m = l + (r - l) // 2
            if search[m][0] > timestamp:
                r = m
            else:
                l = m + 1
        
        return search[l - 1][1] if l > 0 else ""

        
