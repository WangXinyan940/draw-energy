import numpy as np


class Profile:

    def __init__(self, pathname=None):
        self.states = []
        self.pathname = pathname

    def addState(self, energy, name=None, index=None):
        if index is None:
            if len(self.states) == 0:
                idx = 0
            else:
                idx = max([i[2] for i in self.states]) + 1
        self.states.append([energy, name, idx])


class Style:

    def __init__(self):
        pass


def readFile(fname):
    with open(fname, "r") as f:
        text = f.readlines()
    text = [i.strip().split() for i in text if len(i.strip().split()) != 0]
    profs = []
    style = Style()
    for line in text:
        if line[0].upper() == "PROFILE":
            if "PNAME" in line[1].upper():
                p = Profile(pathname=line[1].split(":")[1])
            else:
                p = Profile()
            for state in line[2:]:
                tmp = state.split(":")
                if len(tmp) == 2:
                    e, nm = tmp
                elif len(tmp) == 1:
                    e = tmp
                    nm = None
                e = float(e)
                p.addState(e, name=nm)

        elif line[0].upper() == "STYLE":
            pass #Havent work on it yet.
    return profs, style


def drawCurve(profile, color, line="dash")