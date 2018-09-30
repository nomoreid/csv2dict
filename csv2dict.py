import os
from os.path import isfile, join
import csv

# read csv and make dictionary
# usage :
# ret = CSV2Dict.do('unit.csv','unit_id')
# unit_level = CSV2Dict.do_multi_key('upgrade.csv',('unit_id','level'))
# print(len(ret))

class CSV2Dict:
    def __process(name, path, row_to_dict_fun,header=[]):
        result = {}
        cwd = os.getcwd()
        if path is '':
            path = cwd + '/csv/' + name
        else:
            path = path + '/' + name
        with open(path, mode='r', encoding='utf8') as csvfile:
            reader = csv.reader(csvfile)
            first = True
            for row in reader:
                if  first and len(header)==0 :
                    # if csv's first row is header else you must fill header list.
                    header = list(map(str.lower, row))
                    first = False
                else:
                    row_to_dict_fun(row, header, result)
        return result

    # csv is one key , one value
    def do(csv_file_name, unique_key_name , header=[], make_key_int=False , path=''):
        # make one row process function.
        def make_element(row, header, result):
            element = {}
            for i, val in enumerate(row):
                element[header[i]] = val
            if make_key_int :
                result[int(element[unique_key_name])] = element
            else:
                result[element[unique_key_name]] = element
        return CSV2Dict.__process(csv_file_name, path, make_element , header)

    # csv is multi key , one unique value
    def do_multi_key(csv_file_name, unique_key_names, header=[], make_key_int=False , path=''):
        def make_element(row, header, result):
            element = {}
            for i, val in enumerate(row):
                element[header[i]] = val
            if make_key_int :
                key_list = [int(element[k]) for k in unique_key_names]  
            else:
                key_list = [element[k] for k in unique_key_names]
            # dict key must tuple , not list
            key = tuple(key_list)
            result[key] = element

        return CSV2Dict.__process(csv_file_name, path, make_element , header)