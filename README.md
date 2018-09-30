# csv2dict

read csv and make dictionary
1. usage :
2. ret = CSV2Dict.do('unit.csv','unit_id')  # unique key csv
3. unit_level = CSV2Dict.do_multi_key('upgrade.csv',('unit_id','level')) # multi key csv , key must tuple. 
4. print(len(ret))
