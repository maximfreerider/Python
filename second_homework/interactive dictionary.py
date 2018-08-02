#https://www.codewars.com/kata/interactive-dictionary/train/python
class Dictionary():
    def __init__(self):
        self.d = {}
    def newentry(self, word, definition):
        self.d[word]=definition
    def look(self, key):
        return self.d.get(key) or "Can't find entry for {}".format(key)
