from setuptools import setup, find_packages

setup(
    name="magic_space",
    version="0.1.0",
    description="A tool for managing workspaces.",
    author="Your Name",
    author_email="your.email@example.com",
    url="https://github.com/yourusername/magic_space",
    packages=find_packages(where="."),
    install_requires=[
        "argparse",
    ],
    entry_points={
        "console_scripts": [
            "magic_space = magic_space.main:main",
        ],
    },
    classifiers=[
        "Programming Language :: Python :: 3.11",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
)
