from setuptools import setup

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()
    
setup(name='force_backup_automator',
      version='1.0',
      description='Automates download of the Export Data Weekly Service',
      long_description=long_description,
      long_description_content_type="text/markdown",
      packages=['force_backup_automator'],
      classifiers=[
       "Programming Language :: Python :: 3",
       "License :: OSI Approved :: MIT License",
       "Operating System :: OS Independent",
      ],
      install_requires=[
          'lxml',
          'requests',
          'selenium',
          'beautifulsoup4',
          'urllib3',

      ],
      python_requires='>=3.0',
      zip_safe=False)