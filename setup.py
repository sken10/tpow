import os
from setuptools import setup
import tpow as pkg

pathname = os.path.join(
    os.path.abspath(os.path.dirname(__file__)),
    'README.rst')

desc = open(pathname).read()

setup(
    name = pkg.__name__,
    version = pkg.__version__,
    description = desc.split('\n')[1],
    long_description = desc,
    author = pkg.__author__,
    author_email = 'shirakawa.kenichi@gmail.com',
    url = 'https://github.com/sken10/tpow',
    install_requires = [
        'pyserial>=3.0',
    ],
    packages = [pkg.__name__],
    package_dir = {pkg.__name__: 'tpow'},
    include_package_data = True,
    license = pkg.__license__,
    keywords= '1-wire one-wire USB humidity temperature DS2480 DS18B20 DS2438',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Programming Language :: Python',
        'Topic :: Software Development :: Libraries',
        'Topic :: System :: Hardware :: Hardware Drivers',
    ],
    
)
