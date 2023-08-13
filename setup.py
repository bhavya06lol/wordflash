"""
Usage:
    python setup.py py2app
"""

from setuptools import setup

APP = ['main.py']
APP_NAME = "Word Flash"
DATA_FILES = ['word_flash.ini']

OPTIONS = {
    'argv_emulation': True,
    'plist': {
        'CFBundleName': APP_NAME,
        'CFBundleDisplayName': APP_NAME,
        'CFBundleGetInfoString': "Phonics & Sight Reading Flash Cards",
        'CFBundleIdentifier': "com.metasloan.osx.wordflash",
        'CFBundleVersion': "0.1.0",
        'CFBundleShortVersionString': "0.1.0",
        'NSHumanReadableCopyright': u"Public Domain"
    }
}

setup(
    name=APP_NAME,
    app=APP,
    data_files=DATA_FILES,
    options={'py2app': OPTIONS},
    setup_requires=['py2app'],
)
