#!/usr/bin/env python
"""
Run script for Playwright BDD tests with Behave.
"""
import subprocess
import sys
import os

def main():
    # Get the Python executable
    python_exe = sys.executable
    # Run behave
    cmd = [python_exe, "-m", "behave"]
    if len(sys.argv) > 1:
        cmd.extend(sys.argv[1:])
    result = subprocess.run(cmd, cwd=os.getcwd())
    sys.exit(result.returncode)

if __name__ == "__main__":
    main()