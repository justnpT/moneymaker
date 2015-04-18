from distutils.core import setup

setup(name='strategos',
      version='1.0',
      description='experimental stock analysis tool',
      author='Michal Nowierski',
      packages=['pysocketio == 0.9.6a4'],
      include_package_data = True
)