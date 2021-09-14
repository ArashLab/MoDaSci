from ...task import Task


class Example(Task):

    def execute(self):
        print('Example task has been invoked.')

    def toDict(self):
        return {}  # ToDo
