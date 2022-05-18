def genGrow(pset, min_height, max_height, type_=None, size_limit=150):
    def condition(height, depth):
        return depth < height
    result = generate(pset, min_height, max_height, condition, type_)
    while result is None or len(result) > size_limit:
        result = generate(pset, min_height, max_height, condition, type_)
    return result
