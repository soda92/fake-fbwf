from invoke import task
import shutil, os


def inject_path():
    with open("fbwfmgr.ori.bat", mode="r", encoding="utf-8") as f:
        lines = f.readlines()
        lines = [
            line.replace(
                "{file_path}",
                os.path.join(os.path.dirname(__file__), "fake_fbwf.py"),
            )
            for line in lines
        ]
        with open("fbwfmgr.out.bat", mode="w", encoding="utf-8") as f:
            for line in lines:
                f.write(line)


@task
def dist(c):
    dest = "C:/MYBINDIR"
    inject_path()
    shutil.copy(
        os.path.join(os.path.dirname(__file__), "fbwfmgr.out.bat"),
        os.path.join(dest, "fbwfmgr.bat"),
    )