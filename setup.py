from setuptools import setup, find_packages

with open('README.md', 'r', encoding='utf-8') as fh:
    long_description = fh.read()

setup(
    name='Green_dict',
    version=__version__,
    description='A green dictionary package',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/Supalertee/Green_dict',
    author='Sukrakarn Suaplert',
    author_email='supalertee@gmail.com',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Libraries',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
    ],
    keywords='dictionary, green, development',
    packages=find_packages(exclude=['tests', 'docs']),
    python_requires='>=3.6, <4',
    install_requires=[
        'numpy>=1.18.0',
        'matplotlib>=3.1.0'
    ],
    extras_require={
        'dev': ['check-manifest'],
        'test': ['coverage', 'pytest']
    },
    include_package_data=True,
    entry_points={
        'console_scripts': [
            'green-dict=Green_dict.__main__:main',
        ],
    },
    project_urls={
        'Bug Reports': 'https://github.com/Supalertee/Green_dict/issues',
        'Source': 'https://github.com/Supalertee/Green_dict/',
    },
)
