def solution(files):
    newFiles = []

    for i, file in enumerate(files):
        newFile = [file, "", "", i]
        isHead = True

        for c in file:
            if c.isdigit():
                isHead = False
                newFile[2] += c
            else:
                if isHead:
                    newFile[1] += c.upper()
                else:
                    break
        newFiles.append(newFile)

        newFiles.sort(key=lambda f: (f[1], int(f[2]), f[3]))

    return list(map(lambda f: f[0], newFiles))