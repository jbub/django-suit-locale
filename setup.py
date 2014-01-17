from setuptools import setup, find_packages

with open('README.rst') as fp:
    LONG_DESC = fp.read()

setup(
    name='django-suit-locale',
    url='https://github.com/jbub/django-suit-locale',
    version='1.0.1',
    license='BSD',
    description='Django Suit localization.',
    long_description=LONG_DESC,
    author='Juraj Bubniak',
    author_email='contact@jbub.eu',
    packages=find_packages(),
    include_package_data=True,
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Natural Language :: English',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: Implementation',
        'Programming Language :: Python :: Implementation :: CPython',
        'Programming Language :: Python :: Implementation :: PyPy',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],
)