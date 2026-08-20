---
layout: default
title: Wake Privacy Policy
permalink: /wake/privacy/
published: false
---

# Wake Privacy Policy

> DRAFT - DO NOT PUBLISH until the storage and logging decisions are implemented, all placeholders are resolved, the production build is verified, and legal counsel approves this document.

**Effective date:** {{LEGAL_EFFECTIVE_DATE}}  
**Provider:** Totesoft LLC ("Totesoft," "we," "us," or "our")  
**Notice address:** {{NOTICE_ADDRESS}}  
**Privacy contact:** [{{SUPPORT_CONTACT_EMAIL}}](mailto:{{SUPPORT_CONTACT_EMAIL}})  
**Security contact:** [{{SECURITY_CONTACT_EMAIL}}](mailto:{{SECURITY_CONTACT_EMAIL}})

This Privacy Policy explains how the Wake Jira dashboard gadget accesses, processes, stores, exports, and logs End-User Data. It supplements Totesoft's general privacy policy at {{GENERAL_PRIVACY_POLICY_URL}}. Where this app-specific policy and the general policy differ about Wake, this app-specific policy controls for Wake.

## 1. Scope and roles

Wake is an Atlassian Forge dashboard gadget. A user selects a saved Jira filter and display fields. Wake retrieves matching issues, displays a table, groups issues, calculates counts or numeric aggregates, and creates charts. Licensed functionality may add nested grouping, additional metrics, expanded paging, and CSV export.

{{DATA_PROTECTION_ROLE_STATEMENT}}

The customer controls the saved filters, Jira permissions, dashboard access, selected fields, and content stored in Jira.

## 2. Data Wake accesses and processes

Depending on configuration and Jira permissions, Wake may access or process:

- Jira site, user, dashboard, gadget, installation, and license context supplied by Atlassian;
- saved-filter identifiers, names, JQL, descriptions, owners, and share permissions;
- field metadata, including field identifiers, names, and schema information;
- issue identifiers and issue keys;
- configured display and grouping fields;
- standard fields required for display, currently including summary, issue type, status, priority, and subtask information;
- numeric and categorical field values selected by the user;
- user-related Jira fields selected for display or grouping, which may contain names, account identifiers, avatars, or other personal data supplied by Jira;
- date range and grouping configuration;
- counts, sums, averages, grouped results, charts, and other values derived from the issues loaded; and
- technical status, retry, pagination, rate-limit, and error information.

Wake intentionally avoids requesting all Jira fields and is designed to exclude heavy fields such as descriptions, attachments, comments, and worklogs from selectable/display fetches. The customer remains responsible for choosing fields and filters appropriate for dashboard viewers.

## 3. Jira changes and CSV export

Wake is read-only with respect to Jira issues. It does not intentionally create, edit, transition, or delete issues.

When a licensed feature allows CSV export, the export is generated from the issues already loaded and downloaded through the user's browser. Wake does not send the CSV to a Totesoft server. Once downloaded, the file is controlled by the user and the customer's device, browser, storage, security, and retention policies.

## 4. Configuration and Forge hosted storage

Jira dashboard gadget configuration is submitted to and maintained through Atlassian's gadget/Forge configuration mechanisms.

{{WAKE_STORAGE_FINAL_STATEMENT}}

The current source review found a `FRAME_CONFIG` Forge key-value storage path and related hooks that appear unused by the current single-Custom-UI architecture. This paragraph must be removed before publication. The preferred release action is to remove the unused code and `storage:app` scope. If the storage path remains, this policy must identify the exact record, key scope, users who can trigger it, retention, and deletion behavior.

## 5. Application logs and Totesoft access

{{WAKE_LOGGING_FINAL_STATEMENT}}

The reviewed source currently logs some full JQL strings and Jira response-body fragments in error paths. This paragraph must be removed before publication. Production logging should be changed to use redacted identifiers, status codes, counts, and opaque correlation values rather than saved-filter queries or customer response content.

Forge application logs are hosted through Atlassian's developer platform and can be accessed by authorized Totesoft personnel with access to the app's developer environments. Access must be limited to personnel with a support, security, or operational need.

Totesoft does not operate a separate remote application server for Wake. The reviewed manifest declares no external network egress and no third-party analytics or error-reporting service.

## 6. Licensing and payment information

Wake receives license-status information from Atlassian so it can apply licensed or reduced functionality. Wake does not receive payment card details. Marketplace billing, user-tier calculation, orders, renewals, refunds, and payment processing are handled by Atlassian under the customer's relationship with Atlassian.

## 7. Purposes of processing

Totesoft processes the data described above to:

- retrieve and render the selected Jira filter;
- group, aggregate, chart, and export the loaded issue data;
- apply licensed or reduced feature limits;
- preserve gadget configuration through Atlassian's supported mechanisms;
- diagnose rate limits, API failures, invalid configuration, and performance problems;
- respond to support and security requests; and
- maintain, test, and improve Wake.

Totesoft does not sell End-User Data or use Jira issue content for advertising.

## 8. Accuracy and partial datasets

Wake calculations, totals, charts, and exports reflect only the issues actually loaded. A reduced-functionality installation may stop after a configured issue cap, and future licensed versions may also use paging or load-more limits for performance. Wake should visibly identify partial results. Customers must not treat partial gadget results as a complete audit, financial statement, compliance record, or random statistical sample.

Final launch limits: {{WAKE_PAID_FEATURE_LIMITS_CONFIRMATION}}.

## 9. Disclosure and subprocessors

Wake does not send End-User Data to an external Totesoft backend or to independent analytics providers in the reviewed design. Atlassian provides Jira Cloud, Forge execution, configuration, licensing context, logging, and any Forge hosted storage retained in the final build. Atlassian's processing is governed by the customer's agreement with Atlassian and Atlassian's applicable privacy, security, and subprocessor terms.

Totesoft may disclose information when required by law, to protect legal rights or security, or with the customer's authorization. If Totesoft later adds external egress, analytics, remote processing, or another subprocessor, this policy and the Marketplace Privacy and Security answers must be updated before release.

## 10. Retention and deletion

- **Issue data:** processed during gadget loading and rendering. Wake should not persist issue content in app storage after the storage cleanup recommended above.
- **Gadget configuration:** remains under Atlassian's dashboard/gadget behavior until the gadget, dashboard, installation, or related Atlassian data is changed or removed.
- **Forge logs:** retained for {{FORGE_LOG_RETENTION_PERIOD}}. Any diagnostic material copied into a support ticket must follow Totesoft's approved support-ticket retention rule.
- **Forge hosted storage, if retained:** Atlassian currently states that hosted storage is soft-deleted and retained for 28 days after uninstall. Reinstall does not automatically restore prior data. With customer consent, Totesoft may request relinking through Atlassian within 21 days of uninstall.
- **Customer-requested deletion:** {{WAKE_DATA_DELETION_PROCESS}}

## 11. Data rights and customer requests

Requests concerning access, correction, deletion, restriction, objection, or portability should be sent to [{{SUPPORT_CONTACT_EMAIL}}](mailto:{{SUPPORT_CONTACT_EMAIL}}). {{DATA_REQUEST_PROCESS}}

Because the customer controls Jira issue content and dashboard access, Totesoft may direct an end user to the relevant customer administrator. Totesoft may require the customer's authorization before disclosing or changing installation-scoped information.

## 12. Security

Wake uses Atlassian Forge execution and Jira permission enforcement. Totesoft applies least-privilege scope review, environment access controls, code review, dependency management, field minimization, and diagnostic minimization appropriate to the app. No method of storage or transmission is completely secure.

Report suspected vulnerabilities to [{{SECURITY_CONTACT_EMAIL}}](mailto:{{SECURITY_CONTACT_EMAIL}}). Do not include sensitive production values in the initial report.

## 13. International transfers and DPA

Information about Totesoft's data protection role, international transfer mechanism, and Data Processing Addendum is available here: {{DPA_URL_OR_NOT_OFFERED}}.

## 14. Changes

Totesoft may update this policy when Wake's functionality, permissions, storage, logging, licensing, legal requirements, or service providers change. The effective date above will be updated. Material changes should also be identified in release notes or other appropriate customer communications.

## 15. Contact

Totesoft LLC  
{{NOTICE_ADDRESS}}  
Privacy and support: [{{SUPPORT_CONTACT_EMAIL}}](mailto:{{SUPPORT_CONTACT_EMAIL}})  
Security: [{{SECURITY_CONTACT_EMAIL}}](mailto:{{SECURITY_CONTACT_EMAIL}})
