---

## layout: default
title: Espresso Privacy Policy
permalink: /espresso/privacy/
published: false

# Espresso Privacy Policy

> DRAFT - DO NOT PUBLISH until all placeholders are resolved, the production build is verified, and legal counsel approves this document.

**Effective date:** August 19, 2026  
**Provider:** Totesoft LLC ("Totesoft," "we," "us," or "our")  
**Notice address:** No 5, Concourse Parkway, Suite 3000, Atlanta, Georgia, 30338
**Privacy contact:** [support@totesoft.com](mailto:support@totesoft.com)  
**Security contact:** [{{SECURITY_CONTACT_EMAIL}}](mailto:{{SECURITY_CONTACT_EMAIL}})

This Privacy Policy explains how the Espresso app for Jira Cloud accesses, processes, stores, and logs End-User Data. It supplements Totesoft's general privacy policy at {{GENERAL_PRIVACY_POLICY_URL}}. Where this app-specific policy and the general policy differ about Espresso, this app-specific policy controls for Espresso.

## 1. Scope and roles

Espresso is an Atlassian Forge workflow post function. A Jira administrator configures Espresso on a workflow transition to read two numeric source fields, apply an arithmetic operation, and write the result to a numeric target field.

{{DATA_PROTECTION_ROLE_STATEMENT}}

The customer controls which workflows and fields are configured and remains responsible for the Jira content placed in those fields and for providing required notices to its users.

## 2. Data Espresso accesses and processes

Depending on the customer's configuration and the issue being transitioned, Espresso may access or process:

- Jira site and installation context supplied by Atlassian Forge;
- workflow and post-function configuration, including source field identifiers, target field identifier, and arithmetic operator;
- Jira field metadata, such as field identifiers, names, and types, so administrators can select eligible numeric fields;
- the transitioned issue's identifier and issue key;
- transition identifier and transition name;
- the two configured numeric source values;
- the calculated numeric result and configured target field identifier;
- technical response information from Jira, including status codes and error details; and
- retry count, execution duration, timestamps, and outcome information used for diagnostics.

Espresso does not need issue descriptions, comments, attachments, passwords, personal access tokens, payment card information, or Atlassian account credentials for the functionality described above. Customers should not place sensitive personal information in fields selected for Espresso unless they have an appropriate legal basis and have assessed the app's use.

## 3. Data Espresso writes to Jira

Espresso writes the calculated result to the single configured target field on the transitioned issue. It may request Jira to suppress notifications for this update, but Jira decides whether notification suppression is permitted.

Espresso does not intentionally create comments, attachments, users, projects, or workflow transitions.

## 4. Data stored in Forge hosted storage

Espresso stores a bounded diagnostic history for each rule in Atlassian Forge hosted key-value storage. The current implementation groups a rule by its configured source and target field identifiers and keeps up to 10 recent records for that rule.

A stored run record may contain:

- timestamp;
- issue key;
- transition identifier and transition name;
- operation;
- outcome code and severity;
- user-facing outcome summary;
- truncated technical detail;
- retry count; and
- execution duration.

The storage object also contains an update timestamp. Numeric source values and the calculated target value are not intended to be stored in this run history. Technical error detail should be sanitized before production release so it cannot unintentionally contain customer field content.

Forge hosted storage is partitioned by Atlassian for the app installation. It is not a database directly hosted by Totesoft, and Jira administrators do not have a native interface for browsing the app's raw Forge key-value records.

## 5. Application logs and Totesoft access

Espresso produces Forge application logs for operation, security, and support. In normal operation, logs may include issue keys, field identifiers, transition identifiers, rule identifiers, outcome codes, retry counts, durations, and truncated technical error detail.

{{ESPRESSO_DEBUG_LOGGING_STATEMENT}}

Forge application logs are hosted through Atlassian's developer platform and can be accessed by authorized Totesoft personnel who have access to the app's developer environments. Therefore, it would be inaccurate to state that Totesoft can never access app-related End-User Data. Access must be limited to personnel with a support, security, or operational need and handled under Totesoft's internal access controls.

Totesoft does not operate a separate remote application server for Espresso. The reviewed production design declares no external network egress and no third-party analytics or error-reporting service.

## 6. Purposes of processing

Totesoft processes the data described above to:

- provide and execute the configured calculation;
- show administrators whether a rule recently ran and what outcome occurred;
- validate configuration and troubleshoot field-context, permission, rate-limit, or Jira API failures;
- protect the app and Jira site against invalid or unsafe writes;
- respond to support and security requests; and
- maintain, test, and improve the reliability of Espresso.

Totesoft does not sell End-User Data or use Jira issue content for advertising.

## 7. Disclosure and subprocessors

Espresso does not send End-User Data to an external Totesoft backend or to independent analytics providers in the reviewed design. Atlassian provides Jira Cloud, Forge execution, Forge hosted storage, and Forge logging. Atlassian's processing is governed by the customer's agreement with Atlassian and Atlassian's applicable privacy, security, and subprocessor terms.

Totesoft may disclose information when required by law, to protect legal rights or security, or with the customer's authorization. If Totesoft later adds an external service or subprocessor, this policy and the Marketplace Privacy and Security answers must be updated before that change is released.

## 8. Retention and deletion

- **Workflow configuration:** retained by Jira according to the customer's workflow configuration and Atlassian's product behavior.
- **Run history:** limited by the app to the 10 most recent records per rule. A new record removes the oldest record after the limit is reached.
- **Forge logs:** retained for {{FORGE_LOG_RETENTION_PERIOD}}. Any diagnostic material copied into a support ticket must follow the support-ticket retention rule approved by Totesoft.
- **Uninstallation:** Atlassian currently states that Forge hosted storage is soft-deleted and retained for 28 days after uninstall. Reinstalling does not automatically restore the prior data. With customer consent, Totesoft may request relinking through Atlassian within 21 days of uninstall so Atlassian can process the request before the retention period ends.
- **Customer-requested deletion:** {{ESPRESSO_DATA_DELETION_PROCESS}}

Totesoft will not promise deletion methods that the app or Atlassian platform does not technically provide. Requests may require coordination with the customer's Jira administrator or Atlassian support.

## 9. Data rights and customer requests

Requests concerning access, correction, deletion, restriction, objection, or portability should be sent to [{{SUPPORT_CONTACT_EMAIL}}](mailto:{{SUPPORT_CONTACT_EMAIL}}). {{DATA_REQUEST_PROCESS}}

Because the customer controls the Jira site and issue content, Totesoft may direct an end user to the relevant customer administrator. Totesoft may require the customer's authorization before disclosing or changing installation-scoped data.

## 10. Security

Espresso uses Atlassian Forge execution and hosted storage. Totesoft applies least-privilege scope review, environment access controls, code review, dependency management, and diagnostic minimization appropriate to the app. No method of storage or transmission is completely secure.

Report suspected vulnerabilities to [{{SECURITY_CONTACT_EMAIL}}](mailto:{{SECURITY_CONTACT_EMAIL}}). Do not include sensitive production values in the initial report.

## 11. International transfers and DPA

Information about Totesoft's data protection role, international transfer mechanism, and Data Processing Addendum is available here: {{DPA_URL_OR_NOT_OFFERED}}.

## 12. Changes

Totesoft may update this policy when Espresso's functionality, permissions, storage, logging, legal requirements, or service providers change. The effective date above will be updated. Material changes should also be identified in release notes or other appropriate customer communications.

## 13. Contact

Totesoft LLC  
{{NOTICE_ADDRESS}}  
Privacy and support: [{{SUPPORT_CONTACT_EMAIL}}](mailto:{{SUPPORT_CONTACT_EMAIL}})  
Security: [{{SECURITY_CONTACT_EMAIL}}](mailto:{{SECURITY_CONTACT_EMAIL}})