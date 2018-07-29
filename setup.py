
from setuptools import setup

setup(name='netaggro',
        version='0.1',
        description='Aggregates network statistics about raw network traffic. It does not capture the data for individual packets.',
        url='https://github.com/fuele/netaggro',
        author='fuele',
        author_email='37090676+fuele@users.noreply.github.com',
        license='GPLv2',
        packages=['netaggro'],
        install_requires=[
            'scapy',
            'pytz',
        ],
        zip_safe=False
        )
