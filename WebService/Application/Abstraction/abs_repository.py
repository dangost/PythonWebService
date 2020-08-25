from abc import ABC, abstractmethod


class ARepository:

    object = None

    def __init__(self, obj):
        self.object = obj
        self.load()

    def load(self):
        self.object.load(self.object)

    def add(self, obj):
        self.object.add(self.object, obj)

    def edit(self, id, obj):
        self.object.edit(self.object, id, obj)

    def get(self):
        return self.object.get(self.object)

    def get_id(self, id):
        return self.object.get_id(self.object, id)
