# ADR-0008: Cloud-first Development

## Status

Accepted

## Context

Eira is intended for deployment in schools and community learning centres equipped with Starlink internet connectivity.

The long-term architecture includes a local knowledge base (RAG), while internet connectivity is expected to be available during normal operation.

## Decision

Eira will use a cloud-first inference strategy.

Knowledge retrieval remains local.

Inference is primarily performed through cloud inference providers.

The first supported provider is Groq.

Local language models remain an optional fallback when internet connectivity is unavailable or when local processing is required.

## Motivation

Cloud inference provides:

- Faster responses
- Access to larger models
- Lower hardware requirements during development
- Better user experience
- Freedom to switch inference providers without changing the application architecture

## Consequences

Development will primarily take place on a MacBook Air M4.

The RTX 3060 development machine is repurposed for the Compute-MVP project exploring distributed GPU compute using Vast.ai.

Future deployments may include local GPUs, but Eira's software architecture remains model-independent through a Model Router.

