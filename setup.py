from distutils.core import setup

setup(name='tornadotinyfeedback',
      version='0.1',
      author='David Wilemski',
      author_email='david@davidwilemski.com',
      url='https://github.com/davidwilemski/tornado-tinyfeedback',
      description="A client for tinyfeedback that is compatible with tornado",
      keywords='dashboard, web, graph, metrics, tornado',
      classifiers=['Programming Language :: Python', 'License :: OSI Approved :: BSD License'], # Get strings from http://pypi.python.org/pypi?%3Aaction=list_classifiers
      license='BSD',
      packages=['tornadotinyfeedback'],
      install_requires=['tornado']
      )
