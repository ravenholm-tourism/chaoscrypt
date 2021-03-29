from setuptools import setup

setup(name='chaoscrypt',
      version='0.1',
      description='Stream ciphers using chaotic cryptography',
      url='https://github.com/ravenholm-tourism/chaoscrypt',
      author='Michiel Shortt',
      author_email='michielshortt@gmail.com',
      license='MIT',
      packages=['chaoscrypt'],
      install_requires=[
          'numpy',
          'scipy'
      ],
      zip_safe=False)