import requests


class StudentData():
    def get_data(self):
        data = requests.get("https://hackbulgaria.com/api/students/")
        result = data.json()
        return result


test = StudentData()

if __name__ == "__main__":
    print (test.get_data())
