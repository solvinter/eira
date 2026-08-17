# eira Pilot — Architecture

## Status

Early architecture document. This should describe the system that is actually deployed in the pilot and evolve as implementation decisions are made.

## Initial model

The pilot can be understood as several interacting layers:

```text
people
  ↓
personal and shared devices
  ↓
eira interface / workspaces
  ↓
local network + internet connectivity
  ↓
eira core, retrieval and tools
  ↓
model providers / local compute
  ↓
knowledge and external services
```

## Devices

The architecture may include both personal low-cost devices and more capable shared workstations. Expensive compute should not be duplicated across every user when shared infrastructure can provide the capability more efficiently.

## Connectivity

The system should account for intermittent or constrained connectivity. Functions that benefit from local availability should be identified empirically during the pilot.

## eira

eira provides the interface between users and capabilities such as learning, practical work, repository/code assistance, retrieval, calculation and other workspace-specific tools.

The workspace architecture should allow different contexts to use shared core infrastructure while exposing tools and behaviour appropriate to the task.

## Compute and models

The pilot should measure when fast, economical models are sufficient and when stronger models materially improve outcomes. Routing, retrieval and compact context should be used to avoid unnecessary inference cost.

## Physical infrastructure

The technical architecture includes the physical environment: power, networking, charging, device storage, maintenance, shared workstations and future maker-space equipment where relevant.

## Principle

Architecture should follow observed needs. Add complexity only when the pilot demonstrates a reason for it.
