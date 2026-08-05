# ADR-0001: Local Knowledge First

## Status

Accepted

## Date

2026-08-04

## Context

Eira is designed as an AI platform for education and community development.

The long-term objective is not simply to provide access to a language model, but to build a trusted local knowledge platform.

Language models will evolve rapidly over time.

The value of Eira should therefore not depend on any particular AI model.

Instead, the long-term asset is the local knowledge collected and maintained by the community.

Examples include:

- Ghana NaCCA curriculum
- Teacher Resource Packs
- School policies
- Local educational resources
- Community documentation
- Future Fante and Twi language resources

## Decision

Eira adopts a **Local Knowledge First** architecture.

Knowledge should remain under the control of the local community whenever possible.

Retrieval is performed from locally managed knowledge bases.

Inference may be performed either locally or through cloud providers.

Knowledge ownership is independent of the language model used.

## Motivation

This approach provides:

- Local ownership of educational resources
- Better privacy
- Independence from any AI provider
- Easier verification of answers
- Ability to operate both online and offline
- Long-term sustainability

Language models may change.

The knowledge base remains.

## Consequences

Eira treats the local knowledge base as its primary asset.

Retrieval-Augmented Generation (RAG) is therefore a core architectural component rather than an optional feature.

Future development should prioritise improving the quality of local knowledge over dependence on increasingly capable language models.

