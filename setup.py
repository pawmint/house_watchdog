# -*- coding: utf-8 -*-


from setuptools import setup, find_packages


readme = open('README.md').read()

setup(
    name='House Watchdog',
    version='0.1.0',
    description=("Check whether houses are up/down"),
    long_description=readme,
    author='Romain Endelin',
    author_email='romain.endelin@mines-telecom.fr',
    url='https://github.com/pawmint/house_watchdog.git',
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        'paho-mqtt>=1.0',
        'paramiko>=1.15.2'
    ],
    entry_points = {
        'console_scripts': ['house_watchdog=house_watchdog.watchdog:main'],
    },
    license='Copyright',
    zip_safe=True,  # To be verified
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'Intended Audience :: Science/Research',
        'Natural Language :: English',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Environment :: Console',
        'License :: Other/Proprietary License',
        'Topic :: Scientific/Engineering'
    ],
)
