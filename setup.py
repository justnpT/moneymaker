from setuptools import setup

setup(name='strategos',
      version='1.0',
      description='experimental stock analysis tool',
      author='Michal Nowierski',
      packages=['pysocketio == 0.9.6a4', 'tui == 1.1.1'],
      include_package_data = True
)