class BaseRepository():
    fileName =""

    def __init__(self, file_name) -> None:
        self.fileName = file_name

    def readFile(self):
        with open(self.fileName, mode="r") as f:
            return f.read()

    def writeFile(self, content):
        with open(self.fileName ,mode="w") as f:
            f.write(content)
