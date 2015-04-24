from setuptools import setup, find_packages

setup(name='django-cluster',
      version='0.1',
      description='Run a django microservice cluster in development.',
      url='http://github.com/lander2k2/django-cluster',
      author='Richard Lander',
      author_email='lander2k2@gmail.com',
      license='MIT',
      packages=find_packages(),
      install_requires=['django'],
      zip_safe=False)

