import setuptools

with open('README.md', 'r', encoding='utf-8') as fh:
    long_description = fh.read()

setuptools.setup(
    name='pipeline',
    version='1.0',
    author='William Guimont-Martin',
    author_email='william.guimont-martin.1@ulaval.ca',
    description='Some transforms utilities based on `Arrows` from Haskell',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/willGuimont/pipeline',
    project_urls={
        'Bug Tracker': 'https://github.com/willGuimont/pipeline/issues'
    },
    license='MIT',
    packages=['pipeline'],
    install_requires=[''],
)
