import os
from step.builder.builder import Builder


class Runner:
    def __init__(self, source: str):
        self.source = source

    def run(self):
        if self.source is None:
            raise ValueError("Source file not provided")
        path = os.path.abspath(self.source)
        if not os.path.exists(path):
            raise FileNotFoundError(f"Source file {self.source} not found")

        builder = Builder(path)
        const, settings, steps = builder.build()

        if const is not None:
            const.execute()
        if settings is not None:
            settings.execute()
        if steps is None:
            raise ValueError("No steps found")
        else:
            steps.execute()
