from glob import glob
from os.path import basename
from os.path import splitext

from setuptools import find_packages
from setuptools import setup

setup(
    name='onetimemail',
    version='0.1.0',
    license='MIT',
    description='One-time email address generator.',
    author='Flurin Coretti',
    author_email='hello@flurincoretti.com',
    url='https://github.com/flurincoretti/onetimemail.git',
    packages=find_packages('src'),
    package_dir={'': 'src'},
    py_modules=[splitext(basename(path))[0] for path in glob('src/*.py')],
    zip_safe=False,
    install_requires=[
        'click',
    ],
    entry_points={
        'console_scripts': [
            'otm = onetimemail.onetimemail:cli',
        ]
    },
)