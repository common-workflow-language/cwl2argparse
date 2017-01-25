from setuptools import setup

setup(name="cwl2argparse",
      version="0.1.7",
      description='Generating Python code from CWL tool descriptions with CWL inputs/outputs as argparse arguments',
      author='Anton Khodak',
      author_email='anton.khodak@ukr.net',
      url='https://github.com/common-workflow-language/cwl2argparse',
      install_requires=['jinja2', 'pyyaml'],
      entry_points={
          'console_scripts': [
              'cwl2argparse = cwl2argparse.main:main'
          ]
      },
      packages=['cwl2argparse'],
      classifiers=[
          'Development Status :: 3 - Alpha',
          'Operating System :: POSIX',
          'Intended Audience :: Developers',
          'Environment :: Console',
          'License :: OSI Approved :: Apache Software License',
      ],
      include_package_data=True,
      )
