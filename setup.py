from distutils.core import setup
import py2exe

setup(
    console=[{
    "script":"RepositoryDQProcessor.py",
    version="1.1",
    author="David Katz-Wigmore",
    name="SSVF DQ Repository Processor",
    description="A program to facilitate the processing of the monthly SSVF DQ .pdf files")
