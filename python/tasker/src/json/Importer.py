import json


class Importer:

    def __init__(self):
        pass

    def read_tasks(self):
        # TODO odczytaj plik i zdekoduj treść tutaj
        with open('taski.json', 'r', encoding='utf-8') as file:
            data = json.load(file)
            self.tasks = data
            

    def get_tasks(self):
        # TODO zwróć zdekodowane taski tutaj
        return self.tasks