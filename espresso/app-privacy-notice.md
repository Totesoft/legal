# Espresso — App Privacy Notice

**Provider:** 

Totesoft LLC · [info@totesoft.com](mailto:info@totesoft.com) 

**App:** Espresso (Jira workflow post function, Atlassian Forge) 

**Last updated:** August 19, 2026

This notice describes how the Espresso app handles data in your Jira Cloud site. It supplements the Totesoft privacy policy at [https://www.totesoft.com/privacy-policy](https://www.totesoft.com/privacy-policy). Espresso runs entirely on Atlassian Forge infrastructure; Totesoft operates no servers of its own for this app, and no data is sent to Totesoft or to any third party.

## What the app reads

When an issue passes through a workflow transition on which Espresso is configured, the app reads the two numeric source fields configured for that rule from the transitioned issue, and reads Jira field metadata (field names and types) to identify the configured fields. In the configuration screen, the app lists your site's numeric fields so an administrator can select them.

## What the app writes

The app writes the calculated result to the single configured target numeric field on the transitioned issue. It writes nothing else to your issues.

## What the app stores

For each configured rule, the app keeps a rolling history of the last 10 executions in Atlassian Forge hosted storage, which resides within your own Atlassian site. Each record contains: timestamp, issue key, transition id and name, operation, outcome code, severity, summary, retry count, and duration. **Field values are not stored.**

## What the app logs

Application logs contain field ids, issue keys, and outcome codes for diagnostics. **Field values are never written to logs** in normal operation. The only exception is a debug mode that Totesoft may enable on a specific environment, at a customer's request, during a support investigation.

## What the app does not do

- No data leaves the Atlassian platform: the app makes no network calls to any non-Atlassian host.
- No third-party subprocessors are used beyond Atlassian's own Forge platform.
- No personal data is collected deliberately; issue keys appear in diagnostics as context only.
- No credentials, tokens, or secrets are collected or stored.

## Retention and deletion

Run history is capped at 10 records per rule; older records are overwritten automatically. If the app is uninstalled, data in Atlassian Forge hosted storage is soft-deleted by Atlassian: reinstalling the app within 21 days relinks it to the existing data, and after that window the data is permanently deleted in accordance with Atlassian's standard data retention and disposal policy. Contact us to request earlier removal of stored diagnostics.

## Data subject requests

For access or deletion requests relating to data handled by the app, contact **[info@totesoft.com](mailto:info@totesoft.com)**. Because all app data resides in your own Atlassian site, your Jira administrators can also inspect or remove it directly by uninstalling the app.

## Changes

We will update this notice when the app's data handling changes and revise the date above. Material changes will be noted in the app's release notes.