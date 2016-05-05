# coding: utf-8
"""

license:MIT

Copyright (c) 2016 DKZ

Permission is hereby granted, free of charge, to any person obtaining 
a copy of this software and associated documentation files (the "Software"), 
to deal in the Software without restriction, including without limitation 
the rights to use, copy, modify, merge, publish, distribute, sublicense, 
and/or sell copies of the Software, and to permit persons to whom the Software 
is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included 
in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, 
INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A 
PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT 
HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION 
OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE 
SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

==============================================================================
 ________  __         ______                                                  
|   _____||  |       |_    _|                   _                       _     
|  |      |  |         |  |     _____   __  __ | \_    _______  __  __ | \_   
|  |      |  |         |  |    /     \ |  | | ||   _| |   __  ||  | | ||   _| 
|  |_____ |  |_____   _|  |_  |   o   ||  |_| ||  |___|    ___||  |_| ||  |___
|________||________| |______|  \_____/ |______|\_____/|___|    |______|\_____/
==============================================================================
2016/05/02 by DKZ https://davidkingzyb.github.io

"""

import clio

print(clio.dotitle('CLIoutput'))
print(clio.dohr(20))
print(clio.dotext('list\n'))
print(clio.dolist(['a','b','c']))
print(clio.dolist({'a':1,'b':2,'ccc':333}))
print(clio.dohr(20))
print(clio.dotabel({'a':[1,222,33,33,33,4444],'bbbbbbb':['aa',1,'bbbbbbb','aa','bb'],'cc':['a'],'dd':['d','dd']}))
print(clio.dotabel({'a':[1,222,33,33,33,4444],'bbbbbbb':['aa',1,'bbbbbbb','aa','bb'],'cc':['a'],'dd':['d','dd']},'col'))

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
