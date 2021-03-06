
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

PAGENUM=8

startpage=template%{
    'title':'',
    'con':'\n\n\n\n\n'+clio.dotitle('CLIoutput')+'\n\n                            <'+date+' by DKZ>                \n\n\n',
    'nowpage':1,
    'totalpage':PAGENUM,
    'footer':FOOTER
}

page2=template%{
    'title':clio.dotitle('CLIoutput'),
    'con':"""


                a python lib for making a command line interface
                    and do pretty printing in command line 
        

                                    <by DKZ>


""",
    'nowpage':2,
    'totalpage':PAGENUM,
    'footer':FOOTER
}

page3=template%{
    'title':'LIST',
    'con':"""

        - title

        - list

        - tabel

        - chart

        - ppt





""",
    'nowpage':3,
    'totalpage':PAGENUM,
    'footer':FOOTER
}

page4=template%{
    'title':'USE',
    'con':"""

        import clio
        print(clio.dotext('CLIoutput'))
        print(clio.dohr(20))
        ...

        print(clio.dotitle('CLIoutput'))
        print(clio.dolist(['a','b','c']))
        print(clio.dotabel(d))
        print(clio.dojson(j))
        print(clio.dotree(j))
        print(clio.dobar(c))



""",
    'nowpage':4,
    'totalpage':PAGENUM,
    'footer':FOOTER
}

page5=template%{
    'title':'tree',
    'con':"""

        clio.dotree({'clio':{'clio':['title','tree','list','tabel','ppt','chart'],'clio-pptinit':'clio-pptinit.py','CLIoutput':'CLIoutput'}})

"""+clio.dotree({'clio':{'clio':['title','tree','list','tabel','ppt','chart'],'clio-pptinit':'clio-pptinit.py','CLIoutput':'CLIoutput'}})
,
    'nowpage':5,
    'totalpage':PAGENUM,
    'footer':FOOTER
}

page6=template%{
    'title':'bar chart',
    'con':"""

        clio.dobar({'python':25,'javascript':20,'html':10,'css':5},True)



"""+clio.dobar({'python':25,'javascript':20,'html':10,'css':5},True)+'\n\n\n\n\n',
    'nowpage':6,
    'totalpage':PAGENUM,
    'footer':FOOTER
}


page7=template%{
    'title':'ppt',
    'con':"""

        $python clio-pptinit.py

        edit [yourppttitle].py

        $python [yourppttitle].py









""",
    'nowpage':7,
    'totalpage':PAGENUM,
    'footer':FOOTER
}

endpage=template%{
    'title':'',
    'con':'\n\n\n\n\n'+clio.dotitle('Thanks!')+'\n\n\n\n\n',
    'nowpage':PAGENUM,
    'totalpage':PAGENUM,
    'footer':FOOTER
}
pagearr=[startpage,page2,page3,page4,page5,page6,page7,endpage]
def main():
    print(pagearr[0])
    clio.doppt(0,pagearr)

if __name__ == '__main__':
    main()
