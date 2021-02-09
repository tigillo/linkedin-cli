import setuptools
import os
import shutil

source_directory = os.path.abspath(os.path.dirname(__file__))
with open(os.path.join(source_directory, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()
with open(os.path.join(source_directory, 'linkedin', 'resources', 'version.py'), encoding='utf-8') as f:
    version = f.readline().split('\'')[1]

setuptools.setup(
  name = 'linkedin-cli',
  packages = setuptools.find_packages(),
  version = version,
  description = 'linkedin-cli - Linkedin Command Line Interface',
  long_description=long_description,
  long_description_content_type='text/markdown',
  author = 'tigillo',
  author_email = 'linkedin-cli@tigillo.com',
  url = 'https://linkedin-cli.tigillo.com',
  download_url = 'https://github.com/tigillo/linkedin-cli/archive/' + version + '.tar.gz',
  keywords = ['linkedin', 'linkedin-cli', 'linkedin automation'],
  classifiers = [],
  entry_points = {
    'console_scripts': ['linkedin=linkedin.__main__:main'],
  }
)
