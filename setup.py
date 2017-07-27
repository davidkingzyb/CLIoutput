# coding: utf-8
"""

==============================================================================
 ________  __         ______                                                  
|   _____||  |       |_    _|                   _                       _     
|  |      |  |         |  |     _____   __  __ | \_    _______  __  __ | \_   
|  |      |  |         |  |    /     \ |  | | ||   _| |   __  ||  | | ||   _| 
|  |_____ |  |_____   _|  |_  |   o   ||  |_| ||  |___|    ___||  |_| ||  |___
|________||________| |______|  \_____/ |______|\_____/|___|    |______|\_____/
==============================================================================
2016/09/06 by DKZ https://davidkingzyb.github.io
https://github.com/davidkingzyb/CLIoutput
"""

from setuptools import setup

setup(name='clioutput',
    version='0.1',
    packages=['clio'],
    author='davidkingzyb',
    author_email='davidkingzyb@qq.com',
    license='MIT',
    url='https://pypi.python.org/pypi'
    )

# $ python3 setup.py sdist

# $ python3 setup.py sdist bdist_wheel
# $ twine upload dist/clioutput-0.1-py3-none-any.whl 
