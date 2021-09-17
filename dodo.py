import os
import platform
import shutil
import warnings
from pathlib import Path

DOIT_CONFIG = {
    "default_tasks": ["format", "lint", "test", "prepare_windows_build"],
    "backend": "json",
}

HERE = Path(__file__).parent


def task_format():
    """Reformat all files using black."""
    print(HERE)
    return {"actions": ["isort -y ", ["black", HERE]], "verbosity": 1}


def task_format_check():
    """Check, but not change, formatting using black."""
    return {"actions": [["black", HERE, "--check"]], "verbosity": 1}


def task_lint():
    """Lint all files with Prospector."""
    return {"actions": [["prospector"]], "verbosity": 1}


def task_test():
    """Run Pytest with coverage."""
    return {
        "actions": [["pytest", "--cov=mad_gui", "--cov-config=.coveragerc", "-vv"]],
        "verbosity": 2,
    }


def task_prepare_build():
    """Build a standalone windows executable."""

    import sys

    python_path = sys.executable.split(os.sep)
    venv_path = str(Path(os.sep.join(python_path[:-2])))

    def check_env():
        answer = input(
            "For more information about this message see https://github.com/mad-lab-fau/mad-gui/blob/main/docs/developer_guidelines.rst#6-creating-an-executable."
            f"\n Go on with {venv_path} as the virtual environment exclusively used for packaging? (y/n):"
        )

        if answer.lower() == "n":
            raise ValueError("Aborted by user.")

    def get_dst_path():
        import platform

        arch = platform.system()
        if arch == "Windows":
            return Path(venv_path) / "Lib/site-packages/mad_gui/qt_designer/build/"
        if arch in ["Linux", "Darwin"]:
            python_dirs = os.listdir(Path(venv_path) / "lib/")
            warnings.warn(
                f"dodo.py: Assuming your python 3.7 installation is in {Path(venv_path)}/lib/{python_dirs[0]}"
            )
            return Path(venv_path) / "lib" / python_dirs[0] / "site-packages/mad_gui/qt_designer/build/"
        raise ValueError("What operating system is this?!")

    def set_up_paths():
        if not os.path.exists(get_dst_path().parent):
            raise FileNotFoundError(
                "Apparently mad_gui is not installed in this environemnt. Use `pip install . ` to do so."
            )
        dst_path = get_dst_path()
        os.makedirs(dst_path, exist_ok=True)

    def convert_ui_to_py():
        dst_path = get_dst_path()
        ui_files = [file for file in os.listdir(dst_path.parent) if ".ui" in file]
        print("\n")
        for file in ui_files:
            print(f"Converting from: {dst_path.parent}{os.sep}{file}")
            print(f"To: {dst_path} {os.sep} {file.split('.')[0]}.py\n")
            os.popen(f"pyside2-uic -o {dst_path}{os.sep}{file.split('.')[0]}.py {dst_path.parent}{os.sep}{file}")

        print(
            "Info: These conversion should take place in the virutal environment you are going to use with "
            "pyinstaller."
        )

    return {
        "actions": [check_env, set_up_paths, convert_ui_to_py],
        "verbosity": 2,
    }


def task_docs():
    """Build the documentation."""
    # Delete Autogenerated files from previous run
    shutil.rmtree(str(HERE / "docs/_build"), ignore_errors=True)
    # Copy the images into the docs folder
    os.makedirs(HERE / "docs/_build/html/images/")
    for file in list((HERE / "docs/res/images/").glob("*")):
        shutil.copy(str(file), str(HERE / "docs/_build/html/images/" / str(file).split(os.sep)[-1]))

    # Copy the image buttons
    for file in list((HERE / "mad_gui/qt_designer/images").glob("*.png")):
        shutil.copy(str(file), str(HERE / "docs/_build/html/images/" / str(file).split(os.sep)[-1]))

    if platform.system() == "Windows":
        return {"actions": [[HERE / "docs/make.bat", "html"]], "verbosity": 2}
    return {"actions": [["make", "-C", HERE / "docs", "html"]], "verbosity": 2}
