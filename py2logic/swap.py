class Result():
    data: list[str]

    def __init__(self) -> None:
        self.data = []
    
    def append(self, string: str):
        self.data.append(string)

    def extend(self, strings: list[str]):
        self.data.extend(strings)
    
    def clear(self):
        self.data = []
    
    def replace(self, new_data: list[str]):
        self.data = new_data
    
    def dump(self) -> str:
        res = "\n".join(map(lambda s: s.replace("\n", "\\n"), self.data))
        self.clear()

        return res

result = Result()