# Third-Party Software Component Security Policy

**Organization:** Totesoft LLC
**Policy owner:** [SIVA S THANGARAJ, CEO]
**Effective date:** 09/15/2026
**Review cycle:** Annual, or on material change to the development process
**Version:** 1.0

---

## 1. Purpose

This policy defines how Totesoft evaluates, approves, monitors, and retires third-party software components used in products it develops and distributes. It exists to ensure that security risk introduced by external code is identified before adoption and managed continuously thereafter.

## 2. Scope

This policy applies to all third-party software incorporated into or supporting a Totesoft product, including:

1. Open-source libraries and packages, including transitive dependencies.
2. Commercial software, SaaS platforms, and managed services.
3. Build and CI/CD tooling, including third-party CI actions and container base images.
4. Platform providers on whose infrastructure Totesoft products run.

## 3. Supplier tiering

Third-party components are classified into two tiers, because the assurance that can be obtained differs fundamentally between them.

### Tier 1 — Commercial and contracted suppliers

Suppliers with whom Totesoft holds a commercial or contractual relationship. This includes SaaS vendors, platform providers, managed service providers, and any paid software dependency.

**Requirement: security certification is mandated.** Before a Tier 1 supplier is approved, Totesoft requires the supplier to submit at least one of the following:

1. A current SOC 2 Type II report.
2. A current ISO/IEC 27001 certificate with a statement of applicability.
3. An equivalent recognized attestation, or a current independent penetration test summary where no formal certification exists.

Where a supplier operates a published trust or compliance portal, retrieval of the current report from that portal satisfies this requirement.

Certifications are re-verified annually or on expiry, whichever is sooner. A supplier that cannot produce any of the above is escalated to the policy owner for an explicit, recorded risk-acceptance decision, or is not adopted.

### Tier 2 — Open-source components

Publicly published open-source packages with no contracted supplier.

**Security certifications cannot be mandated from Tier 2 suppliers**, as no commercial relationship or accountable party exists. Totesoft therefore applies the compensating technical controls in Section 4 to every Tier 2 component. This substitution is a deliberate policy position, not an exception.

## 4. Controls applied to open-source components

### 4.1 Pre-adoption review

Before a new direct dependency is introduced, the engineer proposing it confirms and records:

1. **License compatibility** with Totesoft's distribution model.
2. **Maintenance health** — the project shows recent releases, an active maintainer, and a responsive issue tracker.
3. **Known vulnerabilities** — the current version carries no unremediated Critical or High advisory.
4. **Necessity and surface** — the component is required, and no materially smaller or already-adopted alternative serves the purpose.
5. **Transitive footprint** — the dependencies the component brings with it are reviewed alongside it.

Approval is recorded in the pull request introducing the dependency.

### 4.2 Continuous monitoring

1. **Software composition analysis** runs on every pull request and on every branch merged to the default branch, covering all package manifests in the repository.
2. **Automated dependency alerting** is enabled at the repository level and raises pull requests for vulnerable and outdated dependencies on a weekly cadence.
3. **Static analysis** runs on every pull request using security rulesets that include the OWASP Top Ten.
4. **Secret scanning** runs against the repository and its history.

### 4.3 Supply-chain integrity

1. Dependency versions are locked by committed lockfiles; unpinned version ranges are not permitted in a release build.
2. Third-party CI/CD actions are pinned to full 40-character commit SHAs rather than mutable tags or branch references, to prevent silent repointing by the action owner.
3. Updates to pinned references arrive only through reviewed pull requests.

### 4.4 Remediation

| Severity | Remediation target |
|---|---|
| Critical | 7 calendar days |
| High | 30 calendar days |
| Moderate | Next scheduled release |
| Low | Tracked; addressed at maintainer discretion |

Each finding is dispositioned as **Remediate**, **Accept** (with a recorded rationale and expiry), or **False positive** (with a recorded rationale). No finding is closed without a disposition. Where no upstream fix exists within the target window, the component is assessed for replacement or for a compensating control.

### 4.5 Retirement

A component is scheduled for replacement where it becomes unmaintained, where its license terms change incompatibly, or where an unremediated Critical or High advisory persists beyond its target window with no upstream remedy.

## 5. Records

The following are retained and available on request:

1. Dependency inventory per product, derived from committed lockfiles.
2. Dated composition-analysis and static-analysis scan reports.
3. Finding dispositions and risk acceptances.
4. Tier 1 supplier certifications and their verification dates.

Scan evidence is retained for a minimum of 12 months and refreshed before each product release.

## 6. Release gate

No product release is published where an unremediated Critical or High severity finding is present in a shipped component, unless an explicit risk acceptance has been recorded and approved by the policy owner prior to release.

## 7. Responsibilities

| Role | Responsibility |
|---|---|
| Policy owner | Maintains this policy; approves risk acceptances; verifies Tier 1 certifications annually |
| Engineer introducing a dependency | Performs and records the Section 4.1 pre-adoption review |
| Release approver | Confirms the Section 6 gate before publishing |

## 8. Exceptions

Any deviation from this policy requires written approval from the policy owner, with a stated rationale, a compensating control, and an expiry date. Exceptions are reviewed at each policy review.

## 9. Review

This policy is reviewed at least annually. The review confirms that the controls described remain in force and that the tooling referenced remains in use.

---

**Adoption record**

| Version | Date | Author | Change |
|---|---|---|---|
| 1.0 | [Date] | [Name] | Initial adoption |
