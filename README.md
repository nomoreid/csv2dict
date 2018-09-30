# csv2dict

read csv and make dictionary
usage :
. ret = CSV2Dict.do('unit.csv','unit_id')  # unique key csv
. unit_level = CSV2Dict.do_multi_key('upgrade.csv',('unit_id','level')) # multi key csv , key must tuple. 
. if you want make key int , set make_key_int=True
. if header is [] , CSV's first row is header , you can fill custom header , set header=['foo','xxx','aaa']  
