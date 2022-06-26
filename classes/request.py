
# Request  class
class Request:

    def __init__(self, string: str):
        self.info = self._split_string(string)
        self.from_ = self.info[4]
        self.to_ = self.info[6]
        self.amount = int(self.info[1])
        self.product = self.info[2]

    def _split_string(self, string):
        return string.split(' ')

    def __repr__(self):
        return f"Доставить {self.amount} {self.product} из {self.from_} в {self.to_}"
