# eira Pilot — Architecture

## Status

Early architecture document for the first eira pilot. This document should describe the system that is actually deployed and evolve as implementation decisions are tested in practice.

## Pilot scope

The pilot runs for three months with a deliberately small and observable group:

- five students in Class 4
- one teacher
- mathematics as the only subject in scope

The narrow subject scope is intentional. Restricting the pilot to mathematics makes it easier to observe the system closely, review interactions and detect potentially serious deviations or failures before expanding to additional subjects or larger groups.

## Student devices

Each student receives a dedicated Android device with mobile broadband.

The Android devices are configured as eira devices rather than general-purpose smartphones. During the pilot, they should only be usable through eira and the functions explicitly provided as part of the pilot environment.

The initial device model is therefore:

```text
student
  ↓
dedicated Android device
  ↓
mobile broadband
  ↓
eira
  ↓
mathematics homework support
```

The purpose of the device is to make eira continuously accessible to the student for mathematics homework and learning support during the pilot period.

## Teacher

One teacher participates alongside the five students.

The teacher provides an important human reference point for the pilot and helps establish the actual educational context in which eira is being used. Teacher observations should inform the interpretation of student interactions and any changes made during the pilot.

## eira role

In the pilot, eira acts primarily as mathematics homework support for the students.

The pilot is not intended to test every future eira workspace or capability. The goal is to test a narrowly defined real-world learning use case well enough to understand behaviour, quality, reliability, cost and failure modes.

## Model architecture

The pilot initially uses a frontier-model API directly.

This is a deliberate choice. The first objective is to establish the quality and behaviour of the best practical reference system without prematurely optimising around cheaper models.

The initial path is therefore:

```text
student question
      ↓
eira
      ↓
relevant pilot context
      ↓
frontier-model API
      ↓
response
```

The pilot should document actual model usage, latency, cost and answer quality.

## Smaller open and local models

During the pilot, we should document whether economic or infrastructure constraints create a meaningful reason to introduce smaller open models, local models or hybrid routing.

Questions to observe include:

- Is frontier inference economically sustainable at the observed usage level?
- Which interactions could be handled by a smaller model without a meaningful loss of quality?
- Does unreliable or expensive connectivity make local inference materially useful?
- Does local infrastructure such as Starlink, UPS/battery backup or local compute change the economic or reliability trade-off?
- Which tasks should remain on the frontier model even if cheaper alternatives are introduced?

The pilot should not introduce additional model complexity merely because it is technically possible. Smaller or local models should be introduced when observed cost, connectivity, latency or reliability gives a concrete reason to do so.

## Connectivity and power

Each student device initially uses mobile broadband.

Connectivity, charging and power reliability should be observed as part of the deployed system rather than treated as external assumptions. If infrastructure such as Starlink, UPS/battery backup or shared local compute is introduced, its effect on reliability and cost should be documented.

## Pilot duration

The pilot runs for three months.

This period should be long enough to observe repeated real-world use rather than isolated demonstrations, while remaining short and contained enough that problems can be identified before a larger deployment.

## Architecture principle

The first pilot should optimise for observability and learning rather than architectural completeness.

Start with a small group, one subject, dedicated devices and a strong reference model. Add technical complexity only when the pilot produces evidence that it is needed.
