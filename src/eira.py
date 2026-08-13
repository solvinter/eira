from dotenv import load_dotenv

from src.core.workspace_router import route_workspace
from src.workspaces.developer.workspace import run_developer


def main():
    load_dotenv(dotenv_path=".env")

    while True:
        text = input("eira> ").strip()

        if text.casefold() in {"exit", "quit"}:
            break

        workspace, question = route_workspace(text)

        if workspace == "developer":
            answer = run_developer(question)
            print()
            print(answer)
            print()
            continue

        print("Unknown workspace. Try: Developer: <question>")


if __name__ == "__main__":
    main()
