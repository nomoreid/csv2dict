# csv2dict

read csv and make dictionary
usage :
2. ret = CSV2Dict.do('unit.csv','unit_id')  # unique key csv
3. unit_level = CSV2Dict.do_multi_key('upgrade.csv',('unit_id','level')) # multi key csv , key must tuple. 
4. if you want make key int , set make_key_int=True
5. if header is [] , CSV's first row is header , you can fill custom header , set header=['foo','xxx','aaa']  
