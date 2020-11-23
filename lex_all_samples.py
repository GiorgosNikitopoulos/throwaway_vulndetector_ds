import glob
import re
import parse
import subprocess

def main():
    for filepath in glob.glob('functions_test/**.func', recursive = True):
        f = open(filepath, 'r')
        result = subprocess.run(['node /home/user/c-tokenizer/example/tokens.js'], stdin=f , stdout=subprocess.PIPE, shell=True)
        name = filepath.rsplit('/', 1)[1]
        copy_file = 'lexed_outs/' + name
        f2 = open(copy_file, 'w')
        f2.write(str(result.stdout, 'utf-8'))
        f2.close()
        f.close()


    print('Done')

if __name__ == '__main__':
    main()
