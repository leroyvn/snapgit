import subprocess
import os
import shutil
import re
from pathlib import Path

import click
import yaml


def snap(url, branch_or_tag, outdir=None, filename=None):

    pattern = r"(?P<host>(git@|http(s?)://)" \
              r"([\w\.@]+)(/|:))(?P<owner>[\w,\-,\_]+)/" \
              r"(?P<repo_slug>[\w,\-,\_]+)(.git){0,1}((/){0,1})"
    m = re.match(pattern, url)
    repo_slug = m.groupdict()["repo_slug"]

    zipfilename = filename if filename is not None else \
                  f"{repo_slug}_{branch_or_tag}.zip"

    print(f"Archiving {url}/{branch_or_tag} to {zipfilename}")

    rootdir = os.getcwd()

    # Clone repo
    shallow_clone_cmd = [
        "git", "clone", "-b", branch_or_tag,
        url, "--depth", "1"
    ]
    print(" ".join(shallow_clone_cmd))
    subprocess.run(shallow_clone_cmd)

    # Create archive
    archive_cmd = ["git", "archive", "HEAD", "--format=zip"]

    with open(zipfilename, "w") as zipfile:
        print(f"cd {repo_slug}")
        os.chdir(repo_slug)
        print(" ".join(archive_cmd))
        subprocess.run(archive_cmd, stdout=zipfile)
        print(f"cd {rootdir}")
        os.chdir(rootdir)

    # Move archive to output directory
    if outdir is not None:
        print(f"mv {zipfilename} {outdir}")
        os.makedirs(outdir, exist_ok=True)
        shutil.move(zipfilename, outdir)

    # Cleanup
    print(f"rm -rf {repo_slug}")
    shutil.rmtree(repo_slug)


@click.command()
@click.argument("url", required=False)
@click.option("-b", "--branch-or-tag", default="master",
              help="Branch or tag to archive [defaults to master]")
@click.option("-o", "--outdir", default=None,
              help="Directory where to move the archive after its "
                   "creation (missing parent directories will be created)")
@click.option("-f", "--filename", default=None,
              help="Archive file name")
def main(url, branch_or_tag, outdir, filename):
    """
    A simple Git repository snapshot generator. A shallow clone
    of the repository located at URL is created in the current working
    directory and its contents are archived to a zip file.

    If URL is unspecified, the configuration is read from "snapgitrc.yml"
    and flags are ignored.
    """
    if url is not None:
        snap(url, branch_or_tag, outdir)

    else:
        rcfilename = "snapgitrc.yml"
        print(f"Reading settings from {rcfilename}")
        rcfile = yaml.safe_load(open(rcfilename, "r"))

        for settings in rcfile:
            # Collect parameters for rc file
            # -- url: mandatory
            url = settings["url"]

            # -- branch or tag: optional
            for key in ["branch", "tag"]:
                try:
                    branch_or_tag = settings[key]
                except KeyError:
                    continue
                else:
                    break
            else:
                branch_or_tag = "master"

            # -- outdir: optional
            try:
                outdir = settings["outdir"]
            except KeyError:
                outdir = None

            # -- filename: optional
            try:
                filename = settings["filename"]
            except KeyError:
                filename = None

            snap(url, branch_or_tag, outdir, filename)


if __name__ == '__main__':
    main()
