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
try: input = raw_input
except NameError: pass
def doppt(nowpage,pagearr):
    inp=input()
    if inp=='' or inp=='n' or inp=='next':
        nowpage+=1
        if nowpage<len(pagearr):
            print(pagearr[nowpage])
            doppt(nowpage,pagearr)
        else:
            nowpage-=1
            print(pagearr[nowpage])
            print('this is last page.')
            doppt(nowpage,pagearr)
    elif inp=='q' or inp=='quit':
        print('power by CLIoutput , Thanks watching!')
    elif inp=='p' or inp=='prev':
        nowpage-=1
        if nowpage>=0:
            print(pagearr[nowpage])
            doppt(nowpage,pagearr)
        else:
            nowpage=0
            print(pagearr[nowpage])
            print('this is first page.')
            doppt(nowpage,pagearr)
    elif inp=='g' or inp=='go':
        pagenum=input()
        pagenum=int(pagenum)-1
        if pagenum<len(pagearr):
            nowpage=pagenum
            print(pagearr[nowpage])
            doppt(nowpage,pagearr)
        else:
            print('this page is out of range.')
            doppt(nowpage,pagearr)
