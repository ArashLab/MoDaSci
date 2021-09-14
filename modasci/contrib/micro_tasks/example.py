from ...micro_task import MicroTask


class Example(MicroTask):

    def execute(self, volatileData):
        print('Example microtask has been invoked.')
        return volatileData

    def toDict(self):
        return {}  # ToDo
