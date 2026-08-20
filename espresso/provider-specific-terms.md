---
layout: default
title: Espresso Provider-Specific Terms
permalink: /espresso/terms/
published: false
---

# Espresso Provider-Specific Terms

> DRAFT - DO NOT PUBLISH until all placeholders are resolved and legal counsel approves this document.

**Effective date:** {{LEGAL_EFFECTIVE_DATE}}  
**Provider:** Totesoft LLC  
**App:** Espresso for Jira Cloud  
**Marketplace listing:** {{ESPRESSO_MARKETPLACE_URL}}

These Provider-Specific Terms supplement the standard end-user agreement selected for Espresso in Atlassian Marketplace (the "Standard Agreement"). Capitalized terms not defined here have the meanings in the Standard Agreement. If these Provider-Specific Terms conflict with the Standard Agreement, the order of precedence stated in the Standard Agreement applies.

## 1. Espresso service

Espresso is a Jira Cloud workflow post function that an authorized Jira administrator can configure to read two numeric source fields after a workflow transition, apply a supported arithmetic operation, and write the result to a configured numeric target field.

Current supported operations are addition, subtraction, multiplication, and division. Current project support is: {{ESPRESSO_PROJECT_SUPPORT}}.

## 2. Free Marketplace app

Espresso is currently offered as a free Atlassian Marketplace app. Totesoft does not charge a separate Espresso subscription fee under the current listing. Atlassian may still require a customer account and may apply its own platform terms.

Totesoft may introduce optional paid offerings, change the payment model, or discontinue Espresso only in accordance with applicable law, Atlassian Marketplace rules, the Standard Agreement, and any notice obligations. A future paid offering will not apply retroactively without the required customer agreement or Marketplace action.

## 3. Customer responsibilities

The customer is responsible for:

- limiting workflow administration to authorized personnel;
- selecting appropriate source and target fields;
- ensuring the target field is available for the relevant project and issue type;
- testing each rule in a non-production or controlled workflow before broad use;
- reviewing recent-run outcomes and correcting invalid configurations;
- confirming that calculated values are suitable for the customer's business process; and
- maintaining any independent records or backups required by the customer.

Espresso runs after a transition. The target value may update shortly after the issue changes. Empty source fields are not treated as zero. Division by zero and non-finite results are rejected. Precision behavior is: {{ESPRESSO_DIVISION_PRECISION_DECISION}}.

## 4. No professional advice or guaranteed business outcome

Espresso performs configured arithmetic. It does not provide accounting, payroll, tax, legal, medical, safety, or financial advice. The customer must independently verify any value used for compensation, billing, compliance, safety, eligibility, or other material decisions.

## 5. Atlassian platform dependency

Espresso depends on Jira Cloud, Atlassian Forge, Jira REST APIs, workflow behavior, field contexts, permissions, quotas, rate limits, and a Forge workflow post-function module that Atlassian currently labels Preview. Atlassian may change these services. Totesoft will use commercially reasonable efforts to maintain compatibility but does not control Atlassian's platform availability or release schedule.

## 6. Data and privacy

Espresso's data handling is described in the [Espresso Privacy Policy](../privacy/). The customer must not configure Espresso to process data it is not authorized to process.

DPA or data-processing information: {{DPA_URL_OR_NOT_OFFERED}}.

## 7. Support

Support information is available at [Espresso Support](../support/) and {{SUPPORT_URL}}. Unless a separate written support agreement says otherwise, support targets are goals and not service-level guarantees.

## 8. Source code and intellectual property

Espresso and its source code are proprietary to Totesoft LLC unless a specific file or component expressly states a different license. Access to a source repository does not grant a license to copy, modify, distribute, host, resell, or create derivative works beyond rights expressly granted by the Standard Agreement or an applicable open-source license notice.

## 9. Optional governing-law customization

{{GOVERNING_LAW_OVERRIDE_OR_DELETE}}

Delete this section if no override is approved; in that case, the Standard Agreement's default governing-law and venue provisions remain unchanged.

## 10. Notices

Legal notices to Totesoft must be sent to:

Totesoft LLC  
{{NOTICE_ADDRESS}}  
[{{SUPPORT_CONTACT_EMAIL}}](mailto:{{SUPPORT_CONTACT_EMAIL}})
