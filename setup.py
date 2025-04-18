from setuptools import setup, find_packages

VERSION = '0.0.1'
DESCRIPTION = 'function futuristic ui toolkit'

# Setting up
setup(
       # the name must match the folder name 'verysimplemodule'
        name="vortexui",
        version=VERSION,
        author="Raghav Kumar",
        author_email="kumaraghav079@gmail.com",
        description=DESCRIPTION,
        packages=find_packages(),
        install_requires=["pyside6"], # add any additional packages that 
        # needs to be installed along with your package. Eg: 'caer'
)
