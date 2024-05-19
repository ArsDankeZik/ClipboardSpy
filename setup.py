import setuptools
from setuptools.command.install import install
import os

class CustomInstallCommand(install):
    def run(self):
        install.run(self)
        self.create_executable()

    def create_executable(self):
        script_content = '''#!/usr/bin/env python3
import sys
from clipboardspy.clipboardspy import main

if __name__ == "__main__":
    sys.exit(main())
'''
        executable_path = '/usr/local/bin/clipboardspy'
        with open(executable_path, 'w') as f:
            f.write(script_content)
        os.chmod(executable_path, 0o755)

setuptools.setup(
    name='ClipboardSpy',
    version='0.1.0',
    description='A clipboard spy application using GTK4',
    author='Richardo G. Cibea',
    author_email='richardo.gabriel.cibea@gmail.com',
    packages=['clipboardspy'],
    package_dir={'clipboardspy': 'src'},
    package_data={'clipboardspy': ['assets/logo.ico']},
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
    entry_points={
        'console_scripts': [
            'clipboardspy=clipboardspy.clipboardspy:main',
        ],
    },
    include_package_data=True,
    install_requires=[
        'PyGObject',
    ],
    cmdclass={
        'install': CustomInstallCommand,
    },
)
