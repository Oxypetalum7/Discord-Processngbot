import pathlib
import subprocess


def run_sketch():
    path = pathlib.Path('sketch')
    try:
        subprocess.call('processing-java --sketch='+ str(path.resolve()) + ' --run', shell=True)
    except Exception as err:
        print(err)