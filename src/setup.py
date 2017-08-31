from setuptools import setup

setup(
    name='DodgeOrNot',
    version='1.0',
    long_description=__doc__,
    packages=['webserver'],
    include_package_data=True,
    zip_safe=False,
    install_requires=['Flask']
)
