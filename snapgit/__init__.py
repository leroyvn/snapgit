import subprocess
import os
import shutil
import re
from pathlib import Path

import click


def snap(url, branch_or_tag):

    pattern = r"(?P<host>(git@|http(s?)://)" \
              r"([\w\.@]+)(/|:))(?P<owner>[\w,\-,\_]+)/" \
              r"(?P<repo_slug>[\w,\-,\_]+)(.git){0,1}((/){0,1})"
    m = re.match(pattern, url)
    repo_slug = m.groupdict()["repo_slug"]
    zipfilename = f"{repo_slug}_{branch_or_tag}.zip"
    print(f"Archiving {url}/{branch_or_tag} to {zipfilename}")

    shallow_clone_cmd = [
        "git", "clone", "-b", branch_or_tag,
        url, "--depth", "1"
    ]

    archive_cmd = [
        "git", "archive", "HEAD", "--format=zip"
    ]

    rootdir = os.getcwd()

    print(" ".join(shallow_clone_cmd))
    subprocess.run(shallow_clone_cmd)

    with open(zipfilename, "w") as zipfile:
        print(f"cd {repo_slug}")
        os.chdir(repo_slug)
        print(" ".join(archive_cmd))
        subprocess.run(archive_cmd, stdout=zipfile)
        print(f"cd {rootdir}")
        os.chdir(rootdir)

    print(f"rm -rf {repo_slug}")
    shutil.rmtree(repo_slug)


@click.command()
@click.argument("url")
@click.option("-b", "--branch-or-tag", default="master",
              help="Branch or tag to archive [defaults to master]")
def main(url, branch_or_tag):
    """
    A simple Git repository snapshot generator. A shallow clone
    of the repository located at URL is created in the current working
    directory and its contents are archived to a zip file.
    """
    snap(url, branch_or_tag)


if __name__ == '__main__':
    main()
