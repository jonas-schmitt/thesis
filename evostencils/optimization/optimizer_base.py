class Optimizer:
    def __init__(self, program_generator):
        self.program_generator = program_generator
        self.pset = None
        self.toolbox = None
