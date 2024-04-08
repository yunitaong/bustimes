from setuptools import setup, find_packages

setup(
    name='bustimes',
    version='0.1',
    packages=find_packages(),
    install_requires=[
        'requests',
        'ipython'
    ],
    entry_points={
        'console_scripts': [
            'bus-arrival = bus_arrival.bus_arrival:main'
        ]
    },
    author='Rabbit Poop',
    author_email='rabitpoop@gmail.com',
    description='A package to retrieve bus arrival information from LTA DataMall API',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/INSERT/bustimes',
    license='MIT',
)
