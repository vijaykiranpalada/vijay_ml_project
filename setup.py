from setuptools import find_packages,setup
from typing import List
hypen_e_dot='-e .'
#file_path= 'C:\Users\vijay\OneDrive\Desktop\kiran_ml_project'
def get_requirements(file_path:str)->List[str]:
    
    requirements=[]
    with open(file_path)as file_obj:
        requirements=file_obj.readlines()
        requirements=[req.replace('\n',"")for req in requirements]
    if hypen_e_dot in requirements:
        requirements.remove(hypen_e_dot)
    return requirements
setup(
    name='kiran_ml_project',
    version='0.0.1',
    author='vijay',
    author_email='vijaykiran.palada@gmial.com',
    packages=find_packages(),
    install_requirements=get_requirements('requirements.txt')
)