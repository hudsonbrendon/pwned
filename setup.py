from setuptools import setup, find_packages


setup(name='pywned',
      version='0.2.3',
      description='Check if you have an account that'
      'has been compromised in a data breach',
      url='https://github.com/hudsonbrendon/pywned',
      author='Hudson Brendon',
      author_email='contato.hudsonbrendon@gmail.com',
      license='MIT',
      packages=find_packages(exclude=['tests*']),
      install_requires=[
          'requests',
          'ansicolors',
      ],
      entry_points={'console_scripts': ['pywned = pywned:main']},
      zip_safe=False)
