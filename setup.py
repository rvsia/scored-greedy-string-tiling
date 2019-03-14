import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(name='scored-gst-rvsia',
      version='0.1',
      description='An enhanced version of Greed String Tiling algorithm which allows using custom scoring functions',
      long_description=long_description,
      long_description_content_type="text/markdown",
      url='https://github.com/rvsia/scored-greedy-string-tiling',
      author='Richard Vsiansky',
      author_email='r.vsia@seznam.cz',
      license='MIT',
      packages=setuptools.find_packages(),
      classifiers=[
          "Programming Language :: Python :: 3",
          "Programming Language :: Python :: 2",
      ],
      )