import os
from fnmatch import fnmatch


def find_files(pattern: str, root: str):
    paths = []
    for path, subdirs, files in os.walk(root):
        del subdirs
        for name in files:
            if fnmatch(name, pattern):
                paths.append(os.path.join(path, name))
    return paths
