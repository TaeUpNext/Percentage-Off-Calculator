from setuptools import setup

APP = ['Discounted_Price.py']
OPTIONS = { 
'argv_emulation': True,
}

setup(
  app=APP,
  options={'py2app': OPTIONS},
  setup_requires=['py2app']
)