def merge_lists(lst):
    return [item for sublist in lst for item in sublist]

class Optimizer:
    def __init__(self, program_generator, mpi_comm=None, nprocs=1, rank=0):
        self.program_generator = program_generator
        self.pset = None
        self.toolbox = None
        self.params = None
        self.individual_cache = {}
        self.mpi_comm = mpi_comm
        self.nprocs = nprocs
        self.rank = rank

    def is_root(self):
        return self.rank == 0

    def allgather(self, data):
        if self.mpi_comm is None:
            return data
        else:
            return merge_lists(self.mpi_comm.allgather(data))
