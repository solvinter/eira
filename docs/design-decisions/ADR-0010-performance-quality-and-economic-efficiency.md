# ADR-0010: Balance Performance, Capability, and Economic Efficiency

## Status

Accepted

## Context

eira depends on language models and other computational services whose capabilities, latency, and costs vary substantially.

Frontier models can provide excellent reasoning and generation, but their inference remains materially more expensive than smaller or more efficient models. Large contexts, repeated retrieval, unnecessary embeddings, and indiscriminate use of frontier models can also increase both latency and cost.

At the same time, minimising cost at the expense of capability would undermine the product. eira must be fast and capable enough that people genuinely want to use it.

This creates a fundamental architectural balance between:

- performance,
- capability,
- and economic efficiency.

Economic efficiency is therefore not merely an operational concern or a later optimisation. It is a property of the system architecture.

A system whose usefulness depends on subsidising expensive inference indefinitely is not a desirable long-term architecture.

## Decision

eira will be designed to provide the fastest and most capable experience that is economically appropriate for the task.

The system should use the least expensive computational path that can provide a sufficiently good result, while escalating when additional model capability materially improves the outcome.

This principle applies to model selection, retrieval, context construction, agent workflows, and model-to-model handoffs.

### Routing

Workspaces may use different default computational paths.

A workspace does not need to use a frontier model simply because one is available.

Deterministic code should perform tasks that can be solved reliably without model inference.

Smaller or faster models should handle tasks they can perform well.

More capable and expensive models should be used when the task justifies their additional capability.

### Retrieval

Retrieval should be selective.

eira should not retrieve, embed, or transmit large amounts of information merely because that information is available.

Only context likely to improve the result should be introduced into the model context.

### Escalation

Model escalation should preserve useful work already performed.

When a task moves from a faster or less expensive model to a more capable model, eira should normally pass a compact representation of:

- the user's goal,
- established facts,
- relevant constraints,
- work already completed,
- unresolved questions,
- and provenance for important retrieved information.

The stronger model should not automatically receive all raw context previously processed by another model.

It may request additional source material when required.

In this way, eira should escalate understanding rather than blindly duplicate context.

### Performance

Routing and deterministic preprocessing should add negligible perceived latency.

Expensive operations such as model inference, embeddings, retrieval, and large-context processing should only occur when they contribute meaningful value.

Latency should be measured by component so that unnecessary delays can be identified.

### Economics

Model and context cost should be observable and measurable.

Where practical, eira should measure:

- model calls,
- input and output tokens,
- retrieved context size,
- escalation frequency,
- latency,
- and cost per interaction or task.

Optimisation should consider both user experience and economic sustainability.

The objective is not minimum cost.

The objective is the best sustainable relationship between capability, speed, and cost.

## Consequences

eira will not have one universal model pipeline.

Different workspaces may use different combinations of deterministic code, local models, retrieval, cloud models, and frontier models.

Model routing and escalation will become important architectural components.

Context should be treated as a limited computational resource rather than something that should always be maximised.

Experiments should evaluate not only answer quality but also latency and cost.

Some tasks may intentionally use more expensive models when the improvement in quality justifies the cost.

Other tasks should remain entirely local or use inexpensive models when additional capability provides little practical benefit.

## Principle

> eira should be fast and capable enough that people want to use it, and economically efficient enough that people can afford to keep using it.

The long-term goal is a useful and sustainable system rather than one whose operation depends on grants or subsidies to absorb unnecessarily expensive inference.
