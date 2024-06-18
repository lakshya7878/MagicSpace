from setuptools import setup, find_packages

# Read the contents of your README file for the long description
with open("magic_space/README.md", "r", encoding="utf-8") as f:
    long_description = f.read()

setup(
    name="magicspace",
    version="1.0.0",
    description="Fast tool to open a set of apps (workspace) using a single command.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    author="Lakshya Sharma",
    author_email="lakshya7878@gmail.com",
    license="MIT License",
    url="https://github.com/lakshya7878/MagicSpace",
    packages=find_packages(where="."),
    install_requires=[],
    entry_points={
        "console_scripts": [
            "magicspace = magic_space.main:main",
        ],
    },
    classifiers=[
        "Programming Language :: Python :: 3.11",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
)
