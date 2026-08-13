# Experiment: Developer Workspace with Groq 70B

## Status

Planned

## Purpose

Test how capable a fast 70B-class model served through Groq can be as the reasoning engine for eira's Developer workspace.

The goal is not merely to test code generation. The experiment should test whether eira can provide a useful repo-aware developer agent that understands the current project, can inspect relevant source files and Git state, and can reason about what should be done next.

## Hypothesis

A 70B-class model with good local repository tools may be capable of acting as a useful Developer agent without sending the entire repository to the model and without using RAG over the repository.

The surrounding agent architecture may matter as much as model size.

## Initial architecture

    Developer:
        |
        v
    Workspace router
        |
        v
    Local repository tools
        |
        +-- git status / git log
        +-- file listing
        +-- search
        +-- read relevant files
        |
        v
    Context selection
        |
        v
    Groq 70B
        |
        v
    Response / proposed action

The router should add negligible latency.

Repository inspection should happen locally. Only relevant context should be sent to Groq.

## Non-goals

For the initial experiment:

- Do not use RAG over the repository.
- Do not embed the entire repository.
- Do not send the entire repository with every request.
- Do not optimise prematurely for complex autonomous behaviour.
- Do not assume the Groq implementation will become the permanent Developer architecture.

## Initial test questions

1. "Developer: Where are we in the project and what should we do next?"
2. "Developer: How does the router currently work?"
3. "Developer: Find why the RAG pipeline is slow."
4. "Developer: Propose how we could make routing extremely fast."
5. "Developer: Implement this change and show what you changed."

The tests should increase in difficulty from repository understanding to actual code modification.

## Evaluation

Evaluate:

- latency
- quality of repository understanding
- ability to find relevant files
- quality of technical reasoning
- correctness of proposed code changes
- ability to modify code safely
- token usage
- cost
- failures and hallucinations

Where useful, compare the same task with Codex as a reference.

## Design question

The experiment should help answer:

**How much of a capable coding agent comes from the model, and how much comes from the tools and architecture around it?**

## Possible outcome

If the experiment succeeds, the resulting architecture may later be formalised as an ADR for the Developer workspace.

If it fails, document where the 70B model reaches its limits and whether those limitations can reasonably be compensated for by better tools, context management, or agent design.

## Model escalation

A secondary purpose of this experiment is to discover when eira should escalate a task from the default fast model to a more capable model.

The initial principle is:

    Use the fastest adequate model.
    Escalate only when additional capability is likely to improve the result.

The experiment should distinguish between failures caused by:

- insufficient repository context
- inadequate tool use
- poor context selection
- insufficient model reasoning capability
- insufficient coding capability
- uncertainty about the correctness of a proposed change
- tasks whose consequences justify stronger verification

Before escalating, eira should normally attempt to improve the information available to the current model through local repository tools.

Potential escalation signals include:

- repeated unsuccessful attempts
- explicit uncertainty from the model
- inability to resolve conflicting evidence in the repository
- complex changes spanning multiple components
- failure of tests or verification after a proposed change
- tasks requiring substantially deeper reasoning
- high-impact changes where additional verification is valuable

The experiment should record which tasks Groq 70B solves successfully and which tasks benefit materially from escalation to a stronger model.

The long-term goal is not simply to classify models as "good" or "bad", but to develop an empirical routing policy for eira:

    task
      |
      v
    fast/default model
      |
      +-- sufficient --> answer/action
      |
      +-- needs information --> local tools --> retry
      |
      +-- capability limit --> stronger model
      |
      +-- high-impact/uncertain --> stronger verification

This experiment should therefore produce evidence for a future model-routing ADR.
EOF'
