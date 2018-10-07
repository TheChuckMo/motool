"""py_motools setup.py"""

from setuptools import find_packages, setup

setup(
    name='motools',
    version='0.1.0',

    packages=find_packages(exclude=['tests']),

    author='Chuck Mo',
    author_email='chuck@moosejudge.com',

    description='Moosejudge Tools',
    long_description='Chuck experimenting with linear algebra',
    keywords='linear algebra math',
    license='GPLv3',


    #install_requires=[],

    url='https://gitlab.com/TheChuckMo/py_motool',
    project_urls={
        "Source Code": "https://gitlab.com/TheChuckMo/py_motool",
        }
    # Include default config
    #include_package_data=True,
    #package_data={
    #    'config': ['config.yml'],
    #},

    # Setup console script
    # entry_points={
    #     'console_scripts': [
    #         'mocli = motools.app:cli',
    #     ],
    # },

    # sometimes we need more...
)
