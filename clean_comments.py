import glob
import re


def comment_remover(text):
    def replacer(match):
        s = match.group(0)
        if s.startswith('/'):
            return " " # note: a space and not an empty string
        else:
            return s
    pattern = re.compile(
        r'//.*?$|/\*.*?\*/|\'(?:\\.|[^\\\'])*\'|"(?:\\.|[^\\"])*"',
        re.DOTALL | re.MULTILINE
    )
    return re.sub(pattern, replacer, text)

def main():
    for filepath in glob.glob('testcases/**/**.c', recursive = True):
        print(filepath)
        f = open(filepath, "r+")
        text = f.read()
        #print(text)
        f.truncate(0)
        f.write(comment_remover(text))

    print('Done')

    for filepath in glob.glob('testcases/**/**/**.cpp', recursive = True):
        #print(filepath)
        f = open(filepath, "r+")
        text = f.read()
        #print(text)
        f.truncate(0)
        f.write(comment_remover(text))

    print('Done')

    for filepath in glob.glob('testcases/**/**.cpp', recursive = True):
        print(filepath)
        f = open(filepath, "r+")
        text = f.read()
        #print(text)
        f.truncate(0)
        f.write(comment_remover(text))

    print('Done')

    for filepath in glob.glob('testcases/**/**/**.c', recursive = True):
        #print(filepath)
        f = open(filepath, "r+")
        text = f.read()
        #print(text)
        f.truncate(0)
        f.write(comment_remover(text))

    print('Done')

if __name__ == '__main__':
    main()
