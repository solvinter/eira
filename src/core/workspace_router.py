def route_workspace(text):
    workspace, separator, question = text.partition(":")

    if not separator:
        return None, text

    workspace = workspace.strip().casefold()
    question = question.strip()

    if workspace == "developer":
        return "developer", question

    return None, text
