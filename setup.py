'''
the setup.py file is used to specify the dependencies and other metadata for the project. It is used by pip to install the package and its dependencies. The setup.py file should be located in the root directory of the project.
part of package management. It is used to specify the dependencies 
and other metadata for the project. It is used by pip to install the 
package and its dependencies. The setup.py file should be located in
the root directory of the project.
'''

from setuptools import setup, find_packages
from typing import List

def get_requirements()->List[str]:
  requirement_lst: List[str] = []
  try:
    with open('requirements.txt') as file:
          lines= file.readlines()    
          #process the lines to remove any extra whitespace and newline characters
          for line in lines:
              requirement=line.strip()
              ## ignore empty lines and comments and -e
              if requirement and requirement!='-e .' and not requirement.startswith('#'):
                  requirement_lst.append(requirement) 
    return requirement_lst

  except FileNotFoundError:
    print("requirements.txt file not found. Please make sure it exists in the root directory.")
    
setup(
    name='network_security_ml',
    version='0.0.1',
    author='sarmand',
    description='A package for network security machine learning',
    author_email='sarmandfarhad112@gmail.com',
    packages=find_packages(),
    install_requires=get_requirements(),
    python_requires='>=3.8',
    )