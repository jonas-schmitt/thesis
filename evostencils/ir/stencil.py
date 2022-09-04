class Stencil:
    def __init__(self, entries, dimension=None):
        self._dimension = dimension
        self._entries = tuple(entries)

    @property
    def entries(self):
        return self._entries

    @property
    def dimension(self):
        if self._dimension is None:
            return len(self.entries[0][0])
        else:
            return self._dimension

    @property
    def number_of_entries(self):
        return len(self.entries)