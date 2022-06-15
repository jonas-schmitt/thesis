def genGrow(pset, min_height, max_height, type_=None, size_limit=150):
    def condition(height, depth):
        return depth < height
    result = generate(pset, min_height, max_height, condition, type_)
    while len(result) > size_limit:
        # Repeat the process until the generated individual does fulfill the specified limits
        result = generate(pset, min_height, max_height, condition, type_)
    return result
