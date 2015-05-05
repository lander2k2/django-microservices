from setuptools import setup, find_packages

setup(name='django-microservices',
      version='0.1',
      description='A framework for building microservices with Django.',
      url='https://github.com/lander2k2/django-microservices',
      author='Richard Lander',
      author_email='lander2k2@gmail.com',
      license='MIT',
      packages=find_packages(),
      install_requires=['django'],
      zip_safe=False)

