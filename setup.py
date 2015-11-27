from setuptools import setup


setup(
    name='dices',
    version='1.0',
    py_modules=['dices'],
    install_requires=[
        'Click',
    ],
    entry_points='''
        [console_scripts]
        throw=dices:thr
    '''
)
