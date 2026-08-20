---
layout: default
title: Wake Provider-Specific Terms
permalink: /wake/terms/
published: false
---

# Wake Provider-Specific Terms

> DRAFT - DO NOT PUBLISH until all placeholders are resolved and legal counsel approves this document.

**Effective date:** {{LEGAL_EFFECTIVE_DATE}}  
**Provider:** Totesoft LLC  
**App:** Wake for Jira Cloud  
**Marketplace listing:** {{WAKE_MARKETPLACE_URL}}

These Provider-Specific Terms supplement the standard end-user agreement selected for Wake in Atlassian Marketplace (the "Standard Agreement"). Capitalized terms not defined here have the meanings in the Standard Agreement. If these Provider-Specific Terms conflict with the Standard Agreement, the order of precedence stated in the Standard Agreement applies.

## 1. Wake service

Wake is a Jira Cloud dashboard gadget that reads a user-selected saved filter, displays configured issue fields, groups issues, calculates counts or numeric aggregates, and creates charts. Wake is read-only with respect to Jira issues.

## 2. Paid Marketplace app and reduced functionality

Wake is intended to be distributed as a paid-via-Atlassian Marketplace app. Atlassian determines the customer order, licensed user tier, billing, taxes, trial, renewal, cancellation, and refund handling.

When Atlassian reports an active paid or trial license, Wake enables the licensed functionality described in the Marketplace listing. When an active license is not reported, Wake may continue operating with reduced functionality rather than becoming completely unavailable.

The current launch design is:

| Function | Reduced functionality | Active paid/trial license |
|---|---|---|
| Group-by dimensions | 1 | Up to 2 nested dimensions |
| Aggregate metrics | 1 | Multiple metrics under the documented product limits |
| Issues loaded | Up to 500 per gadget load | {{WAKE_PAID_FEATURE_LIMITS_CONFIRMATION}} |
| CSV export | Not available; users may use Jira export | Available, currently limited to 1,000 rows per group |

Final pricing and trial confirmation: {{WAKE_PRICING_CONFIRMATION}}.

The Marketplace listing and order control if they differ from explanatory pricing text in product documentation.

## 3. Customer responsibilities

The customer is responsible for:

- controlling Jira dashboard and saved-filter permissions;
- selecting fields and filters appropriate for dashboard viewers;
- reviewing whether results are complete or partial;
- independently validating values used for material business decisions;
- protecting CSV files after download; and
- testing configuration and performance on representative filters.

## 4. Partial results and technical limits

Wake's tables, groups, totals, averages, counts, charts, and exports use the issues actually loaded. A cap, interrupted crawl, Jira rate limit, permission change, or API failure can produce a partial dataset. Jira search order is not a random sample.

Wake may apply documented limits to columns, nesting, metrics, paging, exports, retries, or refresh frequency to protect reliability, security, and platform cost. Totesoft will describe material customer-facing limits in the listing or documentation.

## 5. No professional advice or guaranteed business outcome

Wake visualizes and calculates Jira data. It does not provide accounting, payroll, tax, legal, medical, safety, financial, or compliance advice. The customer must independently verify any result used for compensation, billing, compliance, safety, eligibility, or another material decision.

## 6. Atlassian platform dependency

Wake depends on Jira Cloud, Atlassian Forge, Jira REST APIs, saved-filter behavior, customer permissions, quotas, rate limits, browser behavior, and Marketplace licensing services. Atlassian may change these services. Totesoft will use commercially reasonable efforts to maintain compatibility but does not control Atlassian's platform availability or release schedule.

## 7. Data and privacy

Wake's data handling is described in the [Wake Privacy Policy](../privacy/). The customer must not configure Wake to process data it is not authorized to process.

DPA or data-processing information: {{DPA_URL_OR_NOT_OFFERED}}.

## 8. Support

Support information is available at [Wake Support](../support/) and {{SUPPORT_URL}}. Unless a separate written support agreement says otherwise, support targets are goals and not service-level guarantees.

## 9. Source code and intellectual property

Wake and its source code are proprietary to Totesoft LLC unless a specific file or component expressly states a different license. Access to a source repository does not grant a license to copy, modify, distribute, host, resell, or create derivative works beyond rights expressly granted by the Standard Agreement or an applicable open-source license notice.

## 10. Optional governing-law customization

{{GOVERNING_LAW_OVERRIDE_OR_DELETE}}

Delete this section if no override is approved; in that case, the Standard Agreement's default governing-law and venue provisions remain unchanged.

## 11. Notices

Legal notices to Totesoft must be sent to:

Totesoft LLC  
{{NOTICE_ADDRESS}}  
[{{SUPPORT_CONTACT_EMAIL}}](mailto:{{SUPPORT_CONTACT_EMAIL}})
