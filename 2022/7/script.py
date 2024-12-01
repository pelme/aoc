import typer


def cwd_path(fs, cwd):
    path = fs

    for dir in cwd:
        path = path[dir]

    return path


def sum_dir(dr):
    size = 0
    small_dirs = 0

    for name, size_or_subdir in dr.items():
        if isinstance(size_or_subdir, int):
            size += size_or_subdir
        else:
            (size_, small_dirs_) = sum_dir(size_or_subdir)
            size += size_
            small_dirs += small_dirs_

    if size < 100000:
        small_dirs += size

    return (size, small_dirs)


@typer.run
def main(input: typer.FileText) -> None:
    fs: dict[str, dict | int] = {}
    cwd: list[str] = []

    for line in input.readlines():
        line = line.strip()

        if line.startswith("$ cd"):
            d = line[5:]
            if d == "/":
                cwd = []
            elif d == "..":
                cwd.pop()
            else:
                cwd.append(d)

        elif line == "$ ls":
            pass

        else:
            current_path = cwd_path(fs, cwd)
            size_or_dir, name = line.split()
            if size_or_dir == "dir":
                current_path[name] = {}
            else:
                current_path[name] = int(size_or_dir)

        current_path = cwd_path(fs, cwd)

    print(sum_dir(fs))
    return None
