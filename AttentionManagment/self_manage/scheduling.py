import os
from itertools import chain
import yaml

class Scheduling:
    def __init__(self):
        self.schedule = None
    def make_schedule(self):
        day_schedule = [None]*24
        day_schedule[14] = "question"
        cwd = os.getcwd()  # Get the current working directory (cwd)
        files = os.listdir(cwd)  # Get all the files in that directory
        print("Files in %r: %s" % (cwd, files))
        #try:
        self.schedule  = yaml.safe_load(open("self_manage/assets/assignment.yaml"))


        for action in self.schedule["actions"]:
            times = action["when"]["prefered"].split("-")
            action_embedded = False

            for i in range(times[0],times[1]):
                if day_schedule[i] is None:
                    day_schedule[i] = action["type"]
                    action_embedded = True


            if not action_embedded:
                concatenated= chain(range(times[1], 23), range(6, times[0]))
                for i in concatenated:
                    if day_schedule[i] is None:
                        day_schedule[i] = action["type"]
                        action_embedded = True








