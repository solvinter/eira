from pathlib import Path
import subprocess


def run_git(repo_root, *args):
    result = subprocess.run(
        ["git", "-C", str(repo_root), *args],
        capture_output=True,
        text=True,
        check=True,
    )
    return result.stdout.strip()


def get_repository_snapshot(repo_root):
    repo_root = Path(repo_root).resolve()

    repo_name = repo_root.name

    branch = run_git(repo_root, "branch", "--show-current")

    status = run_git(repo_root, "status", "--short")
    if not status:
        status = "clean"

    files = run_git(repo_root, "ls-files").splitlines()

    return {
        "repository": repo_name,
        "branch": branch,
        "status": status,
        "files": files,
    }
