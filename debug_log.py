DEBUG = True


def log(*args, **kwargs):
    if DEBUG:
        print(*args, **kwargs)
