# ADR-0009 – Model Router

- **Status:** Proposed
- **Date:** 2026-08-04

## Context

Eira currently uses Groq for language model inference.

Embeddings are generated locally using Ollama (`nomic-embed-text`).

Retrieval is performed locally using an embedded Qdrant vector database.

Future deployments may use Groq, OpenAI, Gemini or other language model providers.

## Decision

All language model providers shall be accessed exclusively through a dedicated Model Router abstraction.

The Model Router is responsible for selecting which language model provider to use based on configuration or future routing logic.

## Motivation

This approach provides:

- Independence from any single AI provider
- Easier experimentation with new models
- Future offline capability using local language models
- Cost optimisation
- Simpler maintenance
- A single interface for all language model providers

## Consequences

Application code shall never communicate directly with a language model provider.

Instead, all requests shall be routed through the Model Router.

New providers should only require implementation inside the Model Router without changes to the rest of the application.

