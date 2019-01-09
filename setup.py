from setuptools import setup

setup(name='fides',
      version='0.0.0',
      description='Fides SDK',
      url='http://github.com/fidestempname/fides-sdk',
      author='asafam',
      author_email='dev@fides.com',
      license='MIT',
      packages=['fides'],
      install_requires=[
          'urllib',
          'lime',
      ],
      zip_safe=False)