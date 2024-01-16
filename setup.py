from setuptools import setup

APP = ["word_generator_ui.py", "main.py"]
DATA_FILES = []
OPTIONS = {
    "argv_emulation": True,
    "packages": ["tkinter", "nltk"],
    "iconfile": "/Users/hassen/local_Dev/Brainstorm_simulator/penguin_logo.icns",  # Path to your .icns file
}

setup(
    app=APP,
    data_files=DATA_FILES,
    options={"py2app": OPTIONS},
    setup_requires=["py2app"],
)
