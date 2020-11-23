import glob
import re
import shutil

def find_start(function_declaration, filename):
    bracket_count = 0
    flag = 0
    f = open(filename, "r")
    text = f.read()
    #print(text)
    entire_func = ""
    while(True):
        start = text.find(function_declaration)
        if(start != -1):
            function_te = text[start:]
            #print(function_te)
            #print('--------------------------------')
            i = 0
            flag = 0
            for letter in function_te:
                #print(letter)
                #print('==============')
                if(letter == '{'):
                    bracket_count = bracket_count + 1
                    flag = 1
                    #print('--------------------------------')
                elif(letter == '}'):
                    bracket_count = bracket_count - 1
                    #print('--------------------------------')
                if bracket_count == 0 and flag == 1:
                    break

                i = i + 1
            #print('++++++++++++++++++++++++')
            #print(function_te[:i+1])
            entire_func = function_te[:i+1]
            #print(entire_func)
            break
            #print('++++++++++++++++++++++++')
        else:
            break
    if(entire_func != ""):
        if (entire_func.splitlines()[0][-1]) == ';':
            entire_func = entire_func.split(';', 1)[1]
        if(entire_func.count('good') < 2 and entire_func.count('bad') < 2):
            #print('==============')
            #print(entire_func)
            return (entire_func)
            #print('==============')
        else:
            return ("")
    return entire_func

def main():
    name_count = 0
    f = open('testcasesupport/testcases.h', "r")
    entire_text = f.read()
    good_list_dirty = entire_text.split('OMITGOOD')[1]
    good_list_dirty = good_list_dirty.split('*/')[1]
    good_list_dirty = good_list_dirty.split('/*')[0]
    split_dirty = good_list_dirty.splitlines()
    for i, line in enumerate(split_dirty):
        split_dirty[i] = line[1:len(line)]
    good_list = [x for x in split_dirty if x]

    bad_list_dirty = entire_text.split('OMITBAD')[1]
    bad_list_dirty = bad_list_dirty.split('*/')[1]
    bad_list_dirty = bad_list_dirty.split('/*')[0]
    split_dirty = bad_list_dirty.splitlines()
    for i, line in enumerate(split_dirty):
        split_dirty[i] = line[1:len(line)]
    bad_list = [x for x in split_dirty if x]

    #for i, function_declaration in enumerate(good_list):
    #    cwe_code = function_declaration.split(' ')[1]
    #    cwe_code = cwe_code.split('_')[0]
    #    function_declaration_clean = function_declaration.split('(')[0]
    #    print(cwe_code)
    for filepath in glob.glob('testcases/**/**.c', recursive = True):
        result = find_start('void ', filepath)
        if(result != ""):
            f = open('functions/' + str(name_count) + '.func', "w")
            f.write(result)
            f.close()
            name_count = name_count + 1
    print('Done')

    for filepath in glob.glob('testcases/**/**/**.cpp', recursive = True):
        result = find_start('void ', filepath)
        if(result != ""):
            f = open('functions/' + str(name_count) + '.func', "w")
            f.write(result)
            f.close()
            name_count = name_count + 1

    print('Done')

    for filepath in glob.glob('testcases/**/**.cpp', recursive = True):
        result = find_start('void ', filepath)
        if(result != ""):
            f = open('functions/' + str(name_count) + '.func', "w")
            f.write(result)
            f.close()
            name_count = name_count + 1
    print('Done')
    for filepath in glob.glob('testcases/**/**/**.c', recursive = True):
        result = find_start('void ', filepath)
        if(result != ""):
            f = open('functions/' + str(name_count) + '.func', "w")
            f.write(result)
            f.close()
            name_count = name_count + 1
    print('Done')
if __name__ == '__main__':
    main()
