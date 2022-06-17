# SnapGit — A simple Git repository snapshot generator

This tool archives the contents of a Git repository given its URL and, optionnally, a branch or a tag name.

## Requirements

The following packages are required:

- PyYaml v5.1 or later
- Click v5.0 or later

## Installation

* Pip, pulling from this repo:
  ```
  pip install git+https://github.com/leroyvn/snapgit.git
  ```

* From source, after cloning this repo:
  ```
  pip install .
  ```

* In a Conda environment, for development, after cloning this repo:
  ```
  mamba env create --file environment.yml
  conda activate snapgit
  pip install --no-deps --editable .
  ```

## Usage

### Simple command line usage

To archive a repository, run:
```
snapgit <url> -b <branch_or_tag>
```
If the `-b` is not used, SnapGit defaults to `master`.

To get help, run:
```
snapgit --help
```

### Using a configuration file

A YAML file can be used. Its contents should be a list of dictionaries, each with the following keys:

- `url`: URL to the repository to be archived
- `tag` or `branch` (optional): tag or branch to use for archiving (defaults to `master`)
- `outdir` (optional): directory where the archive is to be stored
- `filename` (optional): name of the zip archive file
