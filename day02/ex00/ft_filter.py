def ft_filter(f, list_of_inputs):
    if f is not None:
        return [item for item in list_of_inputs if f(item)]
    return [item for item in list_of_inputs if item]
