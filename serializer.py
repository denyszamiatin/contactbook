import json
import csv


class Serializer(object):

    def load(self):
        raise IOError

    def save(self, obj):
        print obj


class JsonSerializer(Serializer):

    def load(self):
        with open('phones.json', 'rt') as f:
            return json.load(f)

    def save(self, obj):
        with open('phones.json', 'wt') as f:
            json.dump(obj, f)


class CsvSerializer(Serializer):

    def load(self):
        obj = {}
        with open('phones.csv', 'rt') as f:
            r = csv.reader(f)
            for name, phone in r:
                obj[name] = phone
        return obj

    def save(self, obj):
        with open('phones.csv', 'wt') as f:
            w = csv.writer(f)
            for name, phone in obj.items():
                w.writerow((name, phone))