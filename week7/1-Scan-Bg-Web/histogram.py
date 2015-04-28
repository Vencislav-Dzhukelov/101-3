import matplotlib.pyplot as plt


class Histogram():

    def __init__(self):
        self.my_dict = {}

    def add(self, name):
        if name not in self.my_dict:
            self.my_dict[name] = 1
        else:
            self.my_dict[name] += 1

    def get_dict(self):
        return self.my_dict

    def count(self, name):
        if name not in self.my_dict.keys():
            return None
        return self.my_dict[name]

    def make_histogram(self, filename):

        with open(filename, "r") as my_file:
            text = my_file.readlines()
            for item in text:
                if "nginx" in item:
                    self.add("nginx")
                if "Apache" in item:
                    self.add("Apache")
                if "IIS" in item:
                    self.add("IIS")
                if "lighttpd" in item:
                    self.add("lighttpd")

        keys = list(self.my_dict.keys())
        values = list(self.my_dict.values())

        X = list(range(len(keys)))

        plt.bar(X, list(self.my_dict.values()), align = "center")
        plt.xticks(X, keys)

        plt.title(".bg servers")
        plt.xlabel("Server")
        plt.ylabel("Count")

        plt.savefig("histogram.png")

h = Histogram()
if __name__ == "__main__":
    h.make_histogram("servers.txt")
    print (h.get_dict())


"""
h = Histogram()
h.add("Apache")
h.add("Apache")
h.add("nginx")
h.add("IIS")
h.add("nginx")
print (h.count("Apache"))
print (h.count("nginx"))
print (h.count("IIS"))
print (h.count("IBM Web Server"))
print (h.get_dict())
"""
