def ft_reduce(f, list_of_inputs, initializer=None):
    if len(list_of_inputs) == 0:
        return initializer
    if initializer is not None:
        list_of_inputs.insert(0, initializer)
    if len(list_of_inputs) == 1:
        return list_of_inputs[0]
    ret = f(list_of_inputs[0], list_of_inputs[1])
    for x in list_of_inputs[2:]:
        ret = f(ret, x)
    return ret
