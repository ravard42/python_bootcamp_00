def ft_map(f, *list_of_inputs):
    f = (lambda *x: x) if f is None else f
    var = list(zip(*list_of_inputs))
    return [f(*i) for i in var]
