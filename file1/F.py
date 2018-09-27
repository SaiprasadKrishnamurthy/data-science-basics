_offsets = {}


def read(file, keyword="") -> None:
    f = open(file=file, encoding='utf-16')
    row = 0
    line = f.readline()
    while len(line) > 0:
        if line.__contains__(keyword):
            if _offsets.__contains__(file):
                _offsets[file][row] = f.tell()
            else:
                _offsets[file] = {}
                _offsets[file][row] = f.tell()
        line = f.readline()
        row += 1
    f.close()


def readRow(file, rowNum) -> str:
    global f
    try:
        f = open(file=file, encoding="utf-16")
        f.seek(_offsets[file][rowNum - 1])
        return f.readline()
    finally:
        f.close()
