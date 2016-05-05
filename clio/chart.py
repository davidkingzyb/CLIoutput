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
2016/05/05 by DKZ https://davidkingzyb.github.io

"""
def dobar(c,ispercent=False,type='col',sign=None,unit=''):
    if not sign:
        if type=='row':
            sign='--'
        else:
            sign='|'
    if ispercent:
        unit='%'

    maxk=0
    total=0
    for k,v in c.iteritems():
        if len(str(k))>maxk:
            maxk=len(str(k))
        total=total+v

    if ispercent:
        for k,v in c.iteritems():
            perv=float(v)/float(total)*100
            c[k]=perv
    output=''
    if type=='row':
        if unit!='':
            output+='unit:'+unit+'\n'
        maxv=0
        for v in c.values():
            if v>maxv:
                maxv=int(v)
        lines=['|  ' for ii in range(maxv)]
        for i in range(len(lines)):
            for k,v in c.iteritems():
                if v>maxv-i:
                    lines[i]+=' '+sign+' '+' '*(maxk-2)
                else:
                    lines[i]+='    '+' '*(maxk-2)
            lines[i]+='\n'
            output+=lines[i]
        output+='|__'+'_'*((maxk+2)*len(c))+'\n   '
        for k in c.keys():
            output+=' '+k+' '+' '*(maxk-len(k))
        output+='\n  '
        for v in c.values():
            output+=' '+str(round(v,2))+' '+' '*(maxk-len(str(round(v))))

    elif type=='col':
        for k,v in c.iteritems():
            output=output+str(k)+' '*(maxk-len(str(k)))+' |  '+sign*int(v)+' '+str(round(v,2))+unit+'\n'
        if unit!='':
            output=output+' unit:'+unit

    return output+'\n'


if __name__ == '__main__':
    c={
        'aaa':10.8,
        'bbbbb':20.5,
        'ccc':14,
        'dddd':30,
        'ee':20,
        'a':2,
    }
    print(dobar(c))
    print(dobar(c,False,'col','$','$'))
    print(dobar(c,True,'col'))
    print(dobar(c,False,'row','$$','$'))
    print(dobar(c,True,'row'))
