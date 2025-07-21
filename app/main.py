from interface.cli_runner import run
import sys

if __name__ == "__main__":
    run(force="--force" in sys.argv)
