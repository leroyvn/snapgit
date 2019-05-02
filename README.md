# SnapGit — A simple Git repository snapshot generator

This tool archives the contents of a Git repository given its URL and, optionnally, a branch or a tag name.

## Installation

From the command line, run:
```bash
$ python setup.py install
```

## Usage

To archive a repository, run:
```
$ snapgit <url> -b <branch_or_tag>
```
If the `-b` is not used, SnapGit defaults to `master`.

To get help, run:
```bash
$ snapgit --help
```