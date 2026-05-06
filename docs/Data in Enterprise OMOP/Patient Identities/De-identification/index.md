---
hide:
  - footer
title: De-identification
---

# De-identification

!!! info "Coming soon"
    This page is a placeholder. Detailed documentation of Emory's de-identification practices for external data sharing is forthcoming.

When clinical data leaves Emory's warehouse for external collaborators — other research institutions, registries, or federated networks — patient identifiers and quasi-identifiers must be removed or transformed to protect patient privacy. Emory's approach follows the [**HIPAA Safe Harbor** method](https://www.hhs.gov/hipaa/for-professionals/privacy/special-topics/de-identification/index.html#safeharborguidance) of de-identification, as defined by HHS.

Substantive de-identification work shipped in v1.0.0 included ZIP3 suppression for patient (non-facility) addresses, removal of PII fields (address lines, city, county), care-site name and source-value masking, and latitude/longitude removal for person-linked locations. Detailed documentation — covering the implementation surface, downstream consumer guidance, and the boundaries between de-identified and limited-data-set release tiers — will land in a future release.

---

[:octicons-arrow-left-24: Patient Identities](../index.md)
