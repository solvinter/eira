from pathlib import Path
import subprocess


def read_file(repo_root, path, start_line=1, end_line=200):
    repo_root = Path(repo_root).resolve()
    file_path = (repo_root / path).resolve()

    if repo_root not in file_path.parents:
        raise ValueError("Path is outside the repository")

    if not file_path.is_file():
        raise FileNotFoundError(f"File not found: {path}")

    lines = file_path.read_text(encoding="utf-8").splitlines()

    start = max(1, start_line)
    end = min(end_line, len(lines))

    selected_lines = lines[start - 1:end]

    return "\n".join(
        f"{line_number}: {line}"
        for line_number, line in enumerate(selected_lines, start=start)
    )


def search_text(repo_root, query, max_results=50):
    repo_root = Path(repo_root).resolve()

    excluded_dirs = {
        ".git",
        ".venv",
        "__pycache__",
        "qdrant_storage",
    }

    results = []

    for file_path in repo_root.rglob("*"):
        if not file_path.is_file():
            continue

        if any(part in excluded_dirs for part in file_path.parts):
            continue

        if file_path.name == ".env":
            continue

        try:
            lines = file_path.read_text(encoding="utf-8").splitlines()
        except (UnicodeDecodeError, OSError):
            continue

        for line_number, line in enumerate(lines, start=1):
            if query.casefold() in line.casefold():
                relative_path = file_path.relative_to(repo_root)

                results.append(
                    f"{relative_path}:{line_number}: {line.strip()}"
                )

                if len(results) >= max_results:
                    return "\n".join(results) + "\n[results truncated]"

    if not results:
        return "No matches found."

    return "\n".join(results)


def search_text(repo_root, query, max_results=50):
    repo_root = Path(repo_root).resolve()

    excluded_dirs = {
        ".git",
        ".venv",
        "__pycache__",
        "qdrant_storage",
    }

    results = []

    for file_path in repo_root.rglob("*"):
        if not file_path.is_file():
            continue

        if any(part in excluded_dirs for part in file_path.parts):
            continue

        if file_path.name == ".env":
            continue

        try:
            lines = file_path.read_text(encoding="utf-8").splitlines()
        except (UnicodeDecodeError, OSError):
            continue

        for line_number, line in enumerate(lines, start=1):
            if query.casefold() in line.casefold():
                relative_path = file_path.relative_to(repo_root)

                results.append(
                    f"{relative_path}:{line_number}: {line.strip()}"
                )

                if len(results) >= max_results:
                    return "\n".join(results) + "\n[results truncated]"

    if not results:
        return "No matches found."

    return "\n".join(results)


def git_status(repo_root):
    repo_root = Path(repo_root).resolve()

    result = subprocess.run(
        ["git", "-C", str(repo_root), "status", "--short"],
        capture_output=True,
        text=True,
        check=True,
    )

    output = result.stdout.strip()

    if not output:
        return "Working tree clean."

    return output


def git_log(repo_root, limit=10):
    repo_root = Path(repo_root).resolve()

    limit = max(1, min(limit, 20))

    result = subprocess.run(
        [
            "git",
            "-C",
            str(repo_root),
            "log",
            f"-{limit}",
            "--oneline",
        ],
        capture_output=True,
        text=True,
        check=True,
    )

    return result.stdout.strip()


def list_files(repo_root, path=".", max_depth=2):
    repo_root = Path(repo_root).resolve()
    target = (repo_root / path).resolve()

    if target != repo_root and repo_root not in target.parents:
        raise ValueError("Path is outside the repository")

    if not target.exists():
        raise FileNotFoundError(f"Path not found: {path}")

    excluded_dirs = {
        ".git",
        ".venv",
        "__pycache__",
        "qdrant_storage",
    }

    results = []

    for item in sorted(target.rglob("*")):
        relative_to_target = item.relative_to(target)

        if len(relative_to_target.parts) > max_depth:
            continue

        if any(part in excluded_dirs for part in item.parts):
            continue

        if item.name == ".env":
            continue

        relative_to_repo = item.relative_to(repo_root)

        if item.is_dir():
            results.append(f"{relative_to_repo}/")
        else:
            results.append(str(relative_to_repo))

    if not results:
        return "No files found."

    return "\n".join(results)
