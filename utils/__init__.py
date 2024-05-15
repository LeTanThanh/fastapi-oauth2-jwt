import sys

paths = (__file__).split("/")
paths.pop()
paths.pop()

ROOT_PATH = "/".join(paths)

sys.path.append(ROOT_PATH)
