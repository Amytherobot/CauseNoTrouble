from setuptools import setup

setup(
    name='causeNoTrouble',
    version='0.1.0',
    entry_points={
        'console_scripts':[
            'causeNoTrouble=causeNoTrouble:run'
        ]
    }

)