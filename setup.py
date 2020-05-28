from setuptools import setup

setup(
    name='web-snooper',
    __version__="1.0.0",
    packages=['web-snooper'],
    package_dir={'web-snooper': 'snooper'},
    entry_points={
        # "name_of_executable = module.with:function_to_execute"
        'console_scripts': [
            'web-snooper = snooper.__main__:main'
        ],
    }
)
