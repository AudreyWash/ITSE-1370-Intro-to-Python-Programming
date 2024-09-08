def skip_integers(*args):
    for arg in args:
        if isinstance(arg, int):
            continue
        print(arg)