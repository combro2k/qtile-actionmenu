import setuptools

from distutils.core import setup

setup(
    name='qtile-actionmenu',
    version='0.1dev',
    packages=['qtileactionmenu',],
    license='Creative Commons Attribution-Noncommercial-Share Alike license',
    long_description=open('README.txt').read(),
    entry_points = {
        'console_scripts': ['qtile-actionmenu=qtileactionmenu.actionmenu:main'],
    },
    install_reuires=[
        'gtk3'                                                                                                                                                     
    ],
)
