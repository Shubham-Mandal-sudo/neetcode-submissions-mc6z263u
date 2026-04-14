class TimeMap:

    def __init__(self):
        self.timeMap = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in list(self.timeMap.keys()):
            self.timeMap[key] = dict()
        self.timeMap[key][timestamp] = value
        return None 

    def get(self, key: str, timestamp: int) -> str:
        if key not in list(self.timeMap.keys()):
            return ""
        else:
            m = -1
            for i in list(self.timeMap[key].keys()):
                if i <= timestamp:
                    m = max(m,i)
            if m == -1:
                return ""
            else:
                return self.timeMap[key][m]
