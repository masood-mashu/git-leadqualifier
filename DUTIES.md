# Separation of Duties for GitLeadQualifier

In accordance with compliance standards and zero-trust engineering principles, all critical operations require dual-party authorization.

## Role Definitions

### Maker
The GrowthMarketingEngineer who sets up inbound lead capture forms and enrichment APIs.

### Checker
The RevenueOperationsDirector who audits lead scoring models, territory splits, and conversion rates.

## Enforcement Mechanism
No configuration, manifest, or policy change evaluated by GitLeadQualifier may be merged without explicit validation by the independent Checker. The system enforces cryptographic integrity across both roles.
