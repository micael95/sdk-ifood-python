import io
from os.path import join, dirname

from setuptools import setup, find_packages


with open('README.md', encoding='utf8') as f:
    long_description = f.read()


setup(
    name='sdk-ifood',
    version='1.0.0.alpha.22',
    license='MIT',
    author='Micael Duarte',
    author_email='dev.etraud@gmail.com',
    packages=find_packages('src'),
    package_dir={'': 'src'},
    include_package_data=True,
    install_requires=['requests'],
    description='SDK com as features da API do IFood',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/etraudm/sdk-ifood-python.git',
    project_urls={
        'Código fonte': 'https://github.com/etraudm/sdk-ifood-python.git'
    },
    keywords='sdk ifood python api merchant financial catalog order developer',
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: Portuguese (Brazilian)',
        'Operating System :: OS Independent',
        'Topic :: Software Development :: Internationalization',
        'Topic :: Scientific/Engineering :: Physics'
    ]
)
