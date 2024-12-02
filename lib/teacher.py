#!/usr/bin/env python
import random

from user import User
knowledge = [
    "str is a data type in Python",
    "programming is hard, but it's worth it",
    "JavaScript async web request",
    "Python function call definition",
    "object-oriented teacher instance",
    "programming computers hacking learning terminal",
    "pipenv install pipenv shell",
    "pytest -x flag to fail fast",
]

import random

class Teacher(User):
    def __init__(self,first_name,last_name):
        super().__init__(first_name,last_name)
        self.knowledge = knowledge
    

    def teach(self):
        # random_index = random.randint(0,len(knowledge) -1)
        # return self.knowledge[random_index]
        return random.choice(self.knowledge)

        pass