# MagicSpace
## Table of Contents
- [Introduction](#introduction)
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Commands](#commands)
- [Contributing](#contributing)

## Introduction

MagicSpace allows user to build different workspaces and open apps in a specific workspace with a single command. This is a fast and lightweight package.

Check out the [magicspace](https://pypi.org/project/magicspace/) project on PyPI.

![Demo GIF](demo.gif)

## Features

- Create different workspaces and add apps to those workspaces
- Delete/List all the workspaces
- Open a workspace by a single command

## Installation

Run the following command in your terminal : 

```bash
pip install magicspace
```

## Usage 

- ##### Commands
    - Create a new workspace : 
        ```bash
        magicspace create <workspace>
        ```
    -   Add apps to a workspace :
        ```bash
        magicspace add --workspace="coding" --apps="VS Code,Google Chrome"
        ```
    - List all workspaces :
        ```bash
        magicspace list
        ```
    - Open a workspace :
        ```bash
        magicspace open <workspace>
        ```
    - Delete a workspace :
        ```bash
        magicspace delete <workspace>
        ```

## Contributing 
- Clone the repo locally :
```bash
git clone https://github.com/lakshya7878/MagicSpace.git
```
- Change directory to : 
```bash
cd magic_space
```
- Run main.py
```bash
python main.py --help
```