import inspect
import pickle


def save(data):
    frame = inspect.stack()[1]
    caller = inspect.getmodule(frame[0])
    modName = str(caller.INFO['name'].replace(" ", "-"))
    path = f'./vault/{modName}.p'
    with open(path, 'wb+') as p:
        pickle.dump(data, p)


def load(blank=None):
    frame = inspect.stack()[1]
    caller = inspect.getmodule(frame[0])
    modName = str(caller.INFO['name'].replace(" ", "-"))
    path = f'./vault/{modName}.p'
    try:
        with open(path, 'rb') as p:
            return pickle.load(p)
    except FileNotFoundError:
        return blank
