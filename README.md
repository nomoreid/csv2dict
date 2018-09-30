# csv2dict

read csv and make dictionary
usage :
ret = CSV2Dict.do('unit.csv','unit_id')
unit_level = CSV2Dict.do_multi_key('upgrade.csv',('unit_id','level'))
print(len(ret))
