import clio
import datetime


PAGENUM=3
date=datetime.datetime.now().strftime('%Y/%m/%d')
FOOTER='by DKZ'

template="""
=================================================================================
%(title)s
---------------------------------------------------------------------------------
%(con)s
----------------------------
%(nowpage)s/%(totalpage)s %(footer)s
"""

startpage=template%{
    'title':'',
    'con':'\n\n\n\n'+clio.dotitle('CLIoutput')+'\n                            <'+date+' by DKZ>                \n\n\n',
    'nowpage':1,
    'totalpage':PAGENUM,
    'footer':FOOTER
}

page2=template%{
    'title':clio.dotitle('CLIoutput'),
    'con':'''


                a python lib for making a command line interface
                    and do pretty printing in command line 
        

                                    <by DKZ>


''',
    'nowpage':2,
    'totalpage':PAGENUM,
    'footer':FOOTER
}

endpage=template%{
    'title':'',
    'con':'\n\n\n\n'+clio.dotitle('Thanks!')+'\n\n\n\n',
    'nowpage':PAGENUM,
    'totalpage':PAGENUM,
    'footer':FOOTER
}

pagearr=[startpage,page2,endpage]

nowpage=0

try: input = raw_input
except NameError: pass

def cliinput():
    global nowpage
    inp=input()
    if inp=='' or inp=='n' or inp=='next':
        nowpage+=1
        if nowpage<len(pagearr):
            print(pagearr[nowpage])
            cliinput()
        else:
            nowpage-=1
            print(pagearr[nowpage])
            print('this is last page.')
            cliinput()
    elif inp=='q' or inp=='quit':
        print('power by CLIoutput , Thanks watching!')
    elif inp=='p' or inp=='prev':
        nowpage-=1
        if nowpage>=0:
            print(pagearr[nowpage])
            cliinput()
        else:
            nowpage=0
            print(pagearr[nowpage])
            print('this is first page.')
            cliinput()
    elif inp=='g' or inp=='go':
        pagenum=input()
        pagenum=int(pagenum)-1
        if pagenum<len(pagearr):
            nowpage=pagenum
            print(pagearr[nowpage])
            cliinput()
        else:
            print('this page is out of range.')
            cliinput()

def main():
    print(pagearr[nowpage])
    cliinput()

if __name__ == '__main__':
    main()