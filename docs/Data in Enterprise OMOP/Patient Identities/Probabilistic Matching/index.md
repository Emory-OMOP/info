---
hide:
  - footer
title: Probabilistic Matching
---

# Probabilistic Matching

!!! info "Coming soon"
    This page is a placeholder for Emory's probabilistic patient-matching methodology — the priors, math derivation, and validated weights — which will be published here for use by other identity-resolution practitioners.

[Patient Identity Stabilization](Patient%20Identity%20Stabilization/index.md) at Emory uses graph-based connected components as its primary mechanism (see [Clustering](Patient%20Identity%20Stabilization/Clustering/index.md)), but a separate body of work has produced **Fellegi-Sunter match weights** calibrated against Emory's identifier landscape. These weights quantify the evidentiary strength of agreement (or disagreement) on individual identifier types — an MRN match between two records is far stronger evidence of identity than, say, a partial-SSN match — and the math derivation makes that explicit and auditable.

The weights were derived from the same identifier evidence pipeline that produces the bronze `merge_evidence_submission` table, with priors anchored to known-true and known-false matches surfaced during the v1.0.0 identity remediation effort. The work is intended to be portable: the priors and derivation are documented in enough detail that another institution running probabilistic matching against EHR data can adapt the framework.

## Forthcoming content

- Definition of the matching agreement vector across Emory identifier types
- Estimation of m-probabilities (agreement given true match) and u-probabilities (agreement given non-match)
- Match-weight calculation and threshold derivation
- Validation against the v1.0.0 ground-truth set
- Adapter notes for practitioners applying this approach in other identity systems

---

[:octicons-arrow-left-24: Patient Identities](../index.md)
