from setuptools import setup


setup(
    name='python_shebang',
    version='0.0.2',
    author='Dwight Hubbard',
    author_email='d@dhub.me',
    packages=['python_shebang'],
    url='',
    license='Apache V2',
    keywords="shebang hashbang ",
    description="Shebang tool to find a compatible python interpreter for a "
                "script",
    long_description=open('README.md').read(),
    classifiers=[
        "Development Status :: 2 - Beta",
        "Topic :: Utilities",
        "License :: OSI Approved :: Apache License V2",
    ],
    scripts=['python_shebang/bin/python_shebang']
)
