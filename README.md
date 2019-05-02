# SnapGit — A simple Git repository snapshot generator

This tool archives the contents of a Git repository given its URL and, optionnally, a branch or a tag name.

## Requirements

The following packages are required:

- PyYaml v5.1 or later
- Click v5.0 or later

## Installation

From the command line, run:
```bash
$ python setup.py install
```

## Usage

### Simple command line usage

To archive a repository, run:
```
$ snapgit <url> -b <branch_or_tag>
```
If the `-b` is not used, SnapGit defaults to `master`.

To get help, run:
```bash
$ snapgit --help
```

### Using a configuration file

A YAML file can be used. Its contents should be a list of dictionaries, each with the following keys:

- `url`: URL to the repository to be archived
- `tag` or `branch` (optional): tag or branch to use for archiving (defaults to `master`)
- `outdir` (optional): directory where the archive is to be stored
- `filename` (optional): name of the zip archive file
