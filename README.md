# CLIoutput

**Command Line Interface Output**

2016/5/1 by DKZ





a python lib for making a command line interface 

and do pretty printing in command line

##List

- [title](#title):a ctfont title
- [list](#list-1):pretty printing list
- [tabel](#tabel):pretty printing table
- [chart](#chart):pretty printing bar chart
- [ppt](#ppt):use clio make ppt

##USE

```py
import clio
print(clio.dotext('CLIoutput\n'))
print(clio.dohr(20))
...

print(clio.dotitle('CLIoutput'))
print(clio.dolist(['a','b','c']))
print(clio.dotabel(d))
print(clio.dojson(j))
print(clio.dotree(j))
print(clio.dobar(c))
```

###title

- dotitle(title)

```
print(clio.dotitle('CLIoutput'))

###################output#####################
 ________  __         ______                                                  
|   _____||  |       |_    _|                   _                       _     
|  |      |  |         |  |     _____   __  __ | \_    _______  __  __ | \_   
|  |      |  |         |  |    /     \ |  | | ||   _| |   __  ||  | | ||   _| 
|  |_____ |  |_____   _|  |_  |   o   ||  |_| ||  |___|    ___||  |_| ||  |___
|________||________| |______|  \_____/ |______|\_____/|___|    |______|\_____/
```

###list

- dolist(arr)

```
print(clio.dolist(['a','b','c']))
print(clio.dolist({'a':1,'b':2,'ccc':333}))

###################output#####################

a
b
c

a    :1
b    :2
ccc  :333
```

###tabel

- dotabel(tabel,t='row',issplit=False)

```
d={
    'a':[1,222,33,33,33,4444],
    'bbbbbbb':['aa',1,'bbbbbbb','aa','bb'],
    'cc':['a'],
    'dd':['d','dd']
  }
print(clio.dotabel(d))
print(clio.dotabel(d,'col'))

###################output#####################
+======+=========+====+====+
| a    | bbbbbbb | dd | cc |
+======+=========+====+====+
| 1    | aa      | d  | a  |
| 222  | 1       | dd |    |
| 33   | bbbbbbb |    |    |
| 33   | aa      |    |    |
| 33   | bb      |    |    |
| 4444 |         |    |    |
+------+---------+----+----+

+---------++----+-----+---------+----+----+------+
| a       || 1  | 222 | 33      | 33 | 33 | 4444 |
+---------++----+-----+---------+----+----+------+
| bbbbbbb || aa | 1   | bbbbbbb | aa | bb |      |
+---------++----+-----+---------+----+----+------+
| dd      || d  | dd  |         |    |    |      |
+---------++----+-----+---------+----+----+------+
| cc      || a  |     |         |    |    |      |
+---------++----+-----+---------+----+----+------+
```

###tree

- dojson(j)
- dotree(j)

```
j={
    'code':0,
    'msg':'hello',
    'result':{
        'a':1,
        'b':2,
        'c':[1,2,3],
    }
}
print(clio.dojson(j))
print(clio.dotree(j))

###################output#####################
{
    "code":0,
    "msg":"hello",
    "result":{
        "a":1,
        "b":2,
        "c":[
            1,
            2,
            3
        ]
    }
}

  |---"code":0
  |---"msg":"hello"
  |---"result":
        |---"a":1
        |---"b":2
        |---"c":
              |---1
              |---2
              |---3
```

###chart

- dobar(c,ispercent=False,type='col',sign=None,unit='')

```
c={
    'aaa':10.8,
    'bbbbb':20.5,
    'ccc':14,
    'dddd':30,
    'ee':20,
    'a':2,
}
print(clio.dobar(c))
print(clio.dobar(c,False,'col','$','$'))
print(clio.dobar(c,True,'col'))
print(clio.dobar(c,False,'row','$$','$'))
print(clio.dobar(c,True,'row'))

###################output#####################
a     |  || 2.0
aaa   |  |||||||||| 10.8
ee    |  |||||||||||||||||||| 20.0
dddd  |  |||||||||||||||||||||||||||||| 30.0
ccc   |  |||||||||||||| 14.0
bbbbb |  |||||||||||||||||||| 20.5


a     |  $$ 2.0$
aaa   |  $$$$$$$$$$ 10.8$
ee    |  $$$$$$$$$$$$$$$$$$$$ 20.0$
dddd  |  $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$ 30.0$
ccc   |  $$$$$$$$$$$$$$ 14.0$
bbbbb |  $$$$$$$$$$$$$$$$$$$$ 20.5$
 unit:$

a     |  || 2.06%
aaa   |  ||||||||||| 11.1%
ee    |  |||||||||||||||||||| 20.55%
dddd  |  |||||||||||||||||||||||||||||| 30.83%
ccc   |  |||||||||||||| 14.39%
bbbbb |  ||||||||||||||||||||| 21.07%
 unit:%

unit:$
|                        $$                  
|                        $$                  
|                        $$                  
|                        $$                  
|                        $$                  
|                        $$                  
|                        $$                  
|                        $$                  
|                        $$                  
|                        $$            $$    
|                 $$     $$            $$    
|                 $$     $$            $$    
|                 $$     $$            $$    
|                 $$     $$            $$    
|                 $$     $$            $$    
|                 $$     $$            $$    
|                 $$     $$     $$     $$    
|                 $$     $$     $$     $$    
|                 $$     $$     $$     $$    
|          $$     $$     $$     $$     $$    
|          $$     $$     $$     $$     $$    
|          $$     $$     $$     $$     $$    
|          $$     $$     $$     $$     $$    
|          $$     $$     $$     $$     $$    
|          $$     $$     $$     $$     $$    
|          $$     $$     $$     $$     $$    
|          $$     $$     $$     $$     $$    
|          $$     $$     $$     $$     $$    
|   $$     $$     $$     $$     $$     $$    
|   $$     $$     $$     $$     $$     $$    
|____________________________________________
    a      aaa    ee     dddd   ccc    bbbbb 
   2.06    11.1   20.55   30.83   14.39   21.07  

unit:%
|                        --                  
|                        --                  
|                        --                  
|                        --                  
|                        --                  
|                        --                  
|                        --                  
|                        --                  
|                        --                  
|                        --            --    
|                 --     --            --    
|                 --     --            --    
|                 --     --            --    
|                 --     --            --    
|                 --     --            --    
|                 --     --            --    
|                 --     --     --     --    
|                 --     --     --     --    
|                 --     --     --     --    
|          --     --     --     --     --    
|          --     --     --     --     --    
|          --     --     --     --     --    
|          --     --     --     --     --    
|          --     --     --     --     --    
|          --     --     --     --     --    
|          --     --     --     --     --    
|          --     --     --     --     --    
|          --     --     --     --     --    
|   --     --     --     --     --     --    
|   --     --     --     --     --     --    
|____________________________________________
    a      aaa    ee     dddd   ccc    bbbbb 
   2.06    11.1   20.55   30.83   14.39   21.07  
```

###ppt

```
$python clio-pptinit.py
title:
testppt
page num:
10

$python testppt.py
<enter>:next page  <p><enter>:prev page  <g><pagenum><enter>go to page num  <q><enter>quit

```

##License

**MIT**

