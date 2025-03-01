from setuptools import find_packages,setup
from typing import List

E_DOT='-e .'
def get_requirements(file_path:str)->List[str]:
    '''
    this function will return the list of requirements
    '''
    requirements=[]
    with open(file_path) as file_obj:
        requirements=file_obj.readlines()
        requirements=[req.replace("\n","") for req in requirements]

        if E_DOT in requirements:
            requirements.remove(E_DOT)
    
    return requirements

setup(
name='Fraud detection',
version='0.0.0',
author='Abraham',
author_email='abrahamowodunni@gmail.com',
packages=find_packages(),
install_requires=get_requirements('requirements.txt')
)