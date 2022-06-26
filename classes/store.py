# Store class
from classes.storage import Storage


class Store(Storage):

    def __init__(self):
        self.items = {}
        self.capacity = 100

    def __repr__(self):
        return "Склад"

    def add(self, title, amount):
        if self.get_free_space() >= amount:
            if title in self.items.keys():
                self.items[title] += amount
                self.capacity -= amount
            else:
                self.items[title] = amount
                self.capacity -= amount
        else:
            print(f"Слишком много, свобоного места осталось {self.capacity}")

    def remove(self, title, amount):
        if (self.items[title] - amount) < 0:
            print(f"Слишком много, всего есть {self.items[title]}")
        else:
            if (self.items[title] - amount) == 0:
                self.items.pop(title)
            else:
                self.items[title] -= amount
                self.capacity += amount

    def get_free_space(self):
        return self.capacity

    def get_items(self):
        return self.items

    def get_unique_items_count(self):
        return len(self.items.keys())
