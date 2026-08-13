import os
import json

from groq import Groq

from src.core.tools.repository_snapshot import get_repository_snapshot
from src.core.tools.repository import (
    read_file,
    search_text,
    list_files,
    git_status,
    git_log,
)


MODEL = "llama-3.3-70b-versatile"


def build_snapshot_text(snapshot):
    files = "\n".join(snapshot["files"])

    return (
        f"Repository: {snapshot['repository']}\n"
        f"Branch: {snapshot['branch']}\n"
        f"Status:\n{snapshot['status']}\n\n"
        f"Tracked files:\n{files}"
    )


TOOLS = [
    {
        "type": "function",
        "function": {
            "name": "read_file",
            "description": "Read selected lines from a file in the eira repository.",
            "parameters": {
                "type": "object",
                "properties": {
                    "path": {"type": "string"},
                    "start_line": {"type": "integer"},
                    "end_line": {"type": "integer"},
                },
                "required": ["path"],
            },
        },
    },
    {
        "type": "function",
        "function": {
            "name": "search_text",
            "description": "Search the eira repository for text.",
            "parameters": {
                "type": "object",
                "properties": {
                    "query": {"type": "string"},
                },
                "required": ["query"],
            },
        },
    },
    {
        "type": "function",
        "function": {
            "name": "list_files",
            "description": "List files in part of the eira repository.",
            "parameters": {
                "type": "object",
                "properties": {
                    "path": {"type": "string"},
                    "max_depth": {"type": "integer"},
                },
            },
        },
    },
    {
        "type": "function",
        "function": {
            "name": "git_status",
            "description": "Show the current Git working-tree status.",
            "parameters": {
                "type": "object",
                "properties": {},
            },
        },
    },
    {
        "type": "function",
        "function": {
            "name": "git_log",
            "description": "Show recent Git commits.",
            "parameters": {
                "type": "object",
                "properties": {
                    "limit": {"type": "integer"},
                },
            },
        },
    },
]


def execute_tool(name, arguments, repo_root):
    if name == "read_file":
        return read_file(
            repo_root,
            arguments["path"],
            arguments.get("start_line", 1),
            arguments.get("end_line", 200),
        )

    if name == "search_text":
        return search_text(
            repo_root,
            arguments["query"],
        )

    if name == "list_files":
        return list_files(
            repo_root,
            arguments.get("path", "."),
            arguments.get("max_depth", 2),
        )

    if name == "git_status":
        return git_status(repo_root)

    if name == "git_log":
        return git_log(
            repo_root,
            arguments.get("limit", 10),
        )

    raise ValueError(f"Unknown tool: {name}")


def run_developer(question, repo_root="."):
    snapshot = get_repository_snapshot(repo_root)

    client = Groq(api_key=os.environ["GROQ_API_KEY"])

    messages = [
        {
            "role": "system",
            "content": (
                "You are eira Developer, a repo-aware development assistant. "
                "Use repository tools when you need evidence. "
                "Do not invent repository contents. "
                "If the initial snapshot is insufficient, request the relevant tool."
            ),
        },
        {
            "role": "user",
            "content": (
                f"{build_snapshot_text(snapshot)}\n\n"
                f"Question:\n{question}"
            ),
        },
    ]

    for _ in range(5):
        response = client.chat.completions.create(
            model=MODEL,
            messages=messages,
            tools=TOOLS,
            tool_choice="auto",
        )

        message = response.choices[0].message

        if not message.tool_calls:
            return message.content

        messages.append(message)

        for tool_call in message.tool_calls:
            name = tool_call.function.name
            arguments = json.loads(tool_call.function.arguments)

            result = execute_tool(
                name,
                arguments,
                repo_root,
            )

            messages.append(
                {
                    "role": "tool",
                    "tool_call_id": tool_call.id,
                    "content": result,
                }
            )

    return "Developer reached the maximum number of tool rounds."
