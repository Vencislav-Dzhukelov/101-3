import json

a = {
    "name": "ivo",
    "age": "22"
}


def serialize_to(path, data):
    json_string = json.dumps(a, indent=4)
    with open(file, "w") as f:
        f.write(json_string)


def unserialize_from(path):
    with open(path, "r") as f:
        contents = f.read()

        return json.loads(contents)
