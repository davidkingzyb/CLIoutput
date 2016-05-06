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
2016/05/06 by DKZ https://davidkingzyb.github.io

"""

output='''
import clio
import datetime

date=datetime.datetime.now().strftime('%Y/%m/%d')
FOOTER=''

template="""
=================================================================================
%(title)s
---------------------------------------------------------------------------------
%(con)s
----------------------------
%(nowpage)s/%(totalpage)s %(footer)s
"""

'''
try: input = raw_input
except NameError: pass
print('title:')
title=input()
print('page num:')
PAGENUM=input()

output+='PAGENUM='+PAGENUM+'\n'

output+='''
startpage=template%{
    'title':'',
    'con':'\\n\\n\\n\\n\\n'+clio.dotitle(\''''+title+'''\')+'\\n\\n                            <'+date+' by DKZ>                \\n\\n\\n',
    'nowpage':1,
    'totalpage':PAGENUM,
    'footer':FOOTER
}
'''

for i in range(int(PAGENUM)):
    if i>1:

        output+='''
page'''+str(i)+'''=template%{
    'title':'title',
    'con':"""















""",
    'nowpage':'''+str(i)+''',
    'totalpage':PAGENUM,
    'footer':FOOTER
}
'''

output+='''
endpage=template%{
    'title':'',
    'con':'\\n\\n\\n\\n\\n'+clio.dotitle('Thanks!')+'\\n\\n\\n\\n\\n',
    'nowpage':PAGENUM,
    'totalpage':PAGENUM,
    'footer':FOOTER
}
'''

output+='pagearr=[startpage,'
for j in range(int(PAGENUM)):
    if j>1:
        output+='page'+str(j)+','

output+='endpage]'
output+='''
def main():
    print(pagearr[0])
    clio.doppt(0,pagearr)

if __name__ == '__main__':
    main()
'''

with open(title+'.py','w') as f:
    f.write(output)
