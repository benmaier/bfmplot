from setuptools import setup

setup(name='bfmplot',
      version='0.0.12',
      description="Snippet collections for plots how I make them.",
      url='https://www.github.com/benmaier/bfmplot',
      author='Benjamin F. Maier',
      author_email='bfmaier@physik.hu-berlin.de',
      license='MIT',
      packages=['bfmplot'],
      install_requires=[
          'numpy>=1.14',
          'scipy>=0.17',
          'matplotlib>=3.3',
      ],
      zip_safe=False)
