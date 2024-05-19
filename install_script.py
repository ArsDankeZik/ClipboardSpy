import os
import subprocess
import sys

def main():
    project_root = os.path.abspath(os.path.dirname(__file__))
    install_prefix = sys.prefix

    os.chdir(project_root)
    subprocess.run([sys.executable, "setup.py", "install", "--prefix", install_prefix])

if __name__ == "__main__":
    main()
