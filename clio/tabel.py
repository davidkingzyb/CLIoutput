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

def dotabel(tabel,t='row'):
    if t=='row':
        output=tabelrow(tabel)
    elif t=='col':
        output=tabelcol(tabel)
    return output

def tabelcol(tabel):
    maxarr=0
    maxtitle=0
    for k,v in tabel.iteritems():
        if len(v)>maxarr:
            maxarr=len(v)
        if len(str(k))>maxtitle:
            maxtitle=len(str(k))
    
    maxlen=[0 for ii in range(maxarr)]
    i=0
    while i<maxarr:
        for v in tabel.values():
            if i<len(v):
                if len(str(v[i]))>maxlen[i]:
                    maxlen[i]=len(str(v[i]))
        i=i+1       
    #print(maxlen)
    hr='+-'+'-'*maxtitle+'-++'
    for x in maxlen:
        hr=hr+'-'+'-'*x+'-+'
    output=hr+'\n'
    for k,v in tabel.iteritems():
        output=output+'| '+str(k)+' '*(maxtitle-len(str(k)))+' ||'
        for j in range(len(maxlen)):
            if j<len(v):
                output=output+' '+str(v[j])+' '*(maxlen[j]-len(str(v[j])))+' |'
            else:
                output=output+' '+' '*maxlen[j]+' |'
        output=output+'\n'+hr+'\n'
    return output
    

def tabelrow(tabel):
    maxlen={}
    linelen=0
    for k in tabel.keys():
        if linelen<len(tabel[k]):
            linelen=len(tabel[k])
        maxlen[k]=len(str(k))
        for x in tabel[k]:
            if maxlen[k]<len(str(x)):
                maxlen[k]=len(str(x))
        #print(k,maxlen[k])
    lines=['' for i in range(linelen*2+3)]
    def addsplit():
        flag=True
        for i in range(len(lines)):
            if flag:
                if i==0 or i==2:
                    lines[i]=lines[i]+'+='
                else:
                    lines[i]=lines[i]+'+-' 
                flag=False
            else:
                lines[i]=lines[i]+'| '
                flag=True
        return lines
    def addcolumn(t,arr):
        flag=True
        for i in range(len(lines)):
            if flag:
                if i==0 or i==2:
                    lines[i]=lines[i]+'='*maxlen[t]+'='
                else:
                    lines[i]=lines[i]+'-'*maxlen[t]+'-'
                flag=False
            else:
                if i==1:
                    lines[i]=lines[i]+str(t)+' '*(maxlen[t]-len(str(t)))+' '
                else:
                    ai=(i-1)/2-1
                    if ai<len(arr):
                        lines[i]=lines[i]+str(arr[ai])+' '*(maxlen[t]-len(str(arr[ai])))+' '
                    else:
                        lines[i]=lines[i]+' '*maxlen[t]+' '
                flag=True
        return lines
    lines=addsplit()
    for k,v in tabel.iteritems():
        lines=addcolumn(k,v)
        lines=addsplit()
    output=''
    for l in lines:
        output=output+l[:-1]+'\n'
    return output





if __name__ == '__main__':
    #tabelcol({'a':[1,222,33,33,33,4444],'bbbbb':['aa',1,'bbbbbbb','aa','bb'],'cc':['a'],'dd':['d','dd']})
    print(dotabel({'a':[1,222,33,33,33,4444],'bbbbbbb':['aa',1,'bbbbbbb','aa','bb'],'cc':['a'],'dd':['d','dd']}))
    print(dotabel({'a':[1,222,3,4444],'bbbbbbb':['aa',1,'bbbbbbb'],'cc':['a'],'dd':['d','dd']},'col'))
