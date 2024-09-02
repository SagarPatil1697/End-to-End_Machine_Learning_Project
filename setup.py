from setuptools import find_packages,setup
from typing import List



HYPEN_E_DOT = '-e .'
def get_requirements(file_path:str)->List[str]:
    """
    this function will return the list of requirements
    """
    requirements = []
    with open(file_path) as f:
        requirements = f.readlines()
        requirements = [req.replace("\n","") for req in requirements]

        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)

setup(
name="End-to-End_ML_Project",
version="0.0.1",
author="Sagar Patil",
author_email="patil.sagar0916@gmail.com",
packages=find_packages(),
install_requires=get_requirements('requirements.txt')

)