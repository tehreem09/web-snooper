from setuptools import setup

setup(
    name='web-snooper',
    __version__="0.0",
    packages=['web-snooper'],
    package_dir={'web-snooper': 'snooper'},
    entry_points={
        # "name_of_executable = module.with:function_to_execute"
        'console_scripts': [
            'web-snooper = snooper.__main__:main'
        ],
    }
)

#   Needed to silence warnings (and to be a worthwhile package)
#     name='Measurements',
#     url='https://github.com/jladan/package_demo',
#     author='John Ladan',
#     author_email='jladan@uwaterloo.ca',
#     # Needed to actually package something
#     packages=['measure'],
#     # Needed for dependencies
#     install_requires=['numpy'],
#     # *strongly* suggested for sharing
#     version='0.1',
#     # The license can be anything you like
#     license='MIT',
#     description='An example of a python package from pre-existing code',
#     # We will also need a readme eventually (there will be a warning)
#     # long_description=open('README.txt').read(),
