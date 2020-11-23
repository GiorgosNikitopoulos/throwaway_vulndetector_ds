import glob
import re
import shutil
import os


def main():
    for i in range(374661):
        #print(i)
        f = open('functions_test/'+ str(i) +'.func', "r")
        entire_text = f.read()
        entire_text = entire_text.lstrip('\n')
        declaration_line = entire_text.split('\n')[0]
        declaration_line = declaration_line.lower()

        if(declaration_line.count('bad') >= 1 and declaration_line.count('good') >= 1):
            good_starting_pos = declaration_line.find('good')
            bad_starting_pos = declaration_line.find('bad')

            if(good_starting_pos < bad_starting_pos):
                old_name = os.path.join("functions_test", str(i) + ".func")
                new_name = os.path.join("functions_test", "good_" + str(i) + ".func")
                os.rename(old_name, new_name)

            if(good_starting_pos > bad_starting_pos):
                old_name = os.path.join("functions_test", str(i) + ".func")
                new_name = os.path.join("functions_test", "bad_" + str(i) + ".func")
                os.rename(old_name, new_name)

            f.close()
            continue

        if(declaration_line.count('bad') >= 1):
            old_name = os.path.join("functions_test", str(i) + ".func")
            new_name = os.path.join("functions_test", "bad_" + str(i) + ".func")
            os.rename(old_name, new_name)

        if(declaration_line.split('\n')[0].count('good') >= 1):
            old_name = os.path.join("functions_test", str(i) + ".func")
            new_name = os.path.join("functions_test", "good_" + str(i) + ".func")
            os.rename(old_name, new_name)
        f.close()


if __name__ == '__main__':
    main()
