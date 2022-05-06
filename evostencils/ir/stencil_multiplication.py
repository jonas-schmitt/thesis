from operator import add as operator_add

def mul(stencil1, stencil2):
    if stencil1 is None or stencil2 is None:
        return None
    new_entries = []
    for offset2, value2 in stencil2.entries:
        for offset1, value1 in stencil1.entries:
            added = False
            offset = tuple(map(operator_add, offset1, offset2))
            value = value1 * value2
            for i, new_entry in enumerate(new_entries):
                if offset == new_entry[0]:
                    new_entries[i] = (offset, new_entry[1] + value)
                    added = True
                    break
            if not added:
                new_entries.append((offset, value))
    return Stencil(new_entries)



