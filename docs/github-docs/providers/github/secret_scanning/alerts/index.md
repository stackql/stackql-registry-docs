---
title: alerts
hide_title: false
hide_table_of_contents: false
keywords:
  - alerts
  - secret_scanning
  - github    
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage GitHub resources using SQL
custom_edit_url: null
image: /img/providers/github/stackql-github-provider-featured-image.png
---

import CopyableCode from '@site/src/components/CopyableCode/CopyableCode';




## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>alerts</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="github.secret_scanning.alerts" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="created_at" /> | `string` | The time that the alert was created in ISO 8601 format: `YYYY-MM-DDTHH:MM:SSZ`. |
| <CopyableCode code="html_url" /> | `string` | The GitHub URL of the alert resource. |
| <CopyableCode code="locations_url" /> | `string` | The REST API URL of the code locations for this alert. |
| <CopyableCode code="number" /> | `integer` | The security alert number. |
| <CopyableCode code="push_protection_bypassed" /> | `boolean` | Whether push protection was bypassed for the detected secret. |
| <CopyableCode code="push_protection_bypassed_at" /> | `string` | The time that push protection was bypassed in ISO 8601 format: `YYYY-MM-DDTHH:MM:SSZ`. |
| <CopyableCode code="push_protection_bypassed_by" /> | `object` | A GitHub user. |
| <CopyableCode code="resolution" /> | `string` | **Required when the `state` is `resolved`.** The reason for resolving the alert. |
| <CopyableCode code="resolution_comment" /> | `string` | An optional comment to resolve an alert. |
| <CopyableCode code="resolved_at" /> | `string` | The time that the alert was resolved in ISO 8601 format: `YYYY-MM-DDTHH:MM:SSZ`. |
| <CopyableCode code="resolved_by" /> | `object` | A GitHub user. |
| <CopyableCode code="secret" /> | `string` | The secret that was detected. |
| <CopyableCode code="secret_type" /> | `string` | The type of secret that secret scanning detected. |
| <CopyableCode code="secret_type_display_name" /> | `string` | User-friendly name for the detected secret, matching the `secret_type`.<br />For a list of built-in patterns, see "[Secret scanning patterns](https://docs.github.com/code-security/secret-scanning/secret-scanning-patterns#supported-secrets-for-advanced-security)." |
| <CopyableCode code="state" /> | `string` | Sets the state of the secret scanning alert. You must provide `resolution` when you set the state to `resolved`. |
| <CopyableCode code="updated_at" /> | `string` | The time that the alert was last updated in ISO 8601 format: `YYYY-MM-DDTHH:MM:SSZ`. |
| <CopyableCode code="url" /> | `string` | The REST API URL of the alert resource. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get_alert" /> | `SELECT` | <CopyableCode code="alert_number, owner, repo" /> | Gets a single secret scanning alert detected in an eligible repository.<br />To use this endpoint, you must be an administrator for the repository or for the organization that owns the repository, and you must use a personal access token with the `repo` scope or `security_events` scope.<br />For public repositories, you may instead use the `public_repo` scope.<br /><br />GitHub Apps must have the `secret_scanning_alerts` read permission to use this endpoint. |
| <CopyableCode code="list_alerts_for_enterprise" /> | `SELECT` | <CopyableCode code="enterprise" /> | Lists secret scanning alerts for eligible repositories in an enterprise, from newest to oldest.<br />To use this endpoint, you must be a member of the enterprise, and you must use an access token with the `repo` scope or `security_events` scope. Alerts are only returned for organizations in the enterprise for which you are an organization owner or a [security manager](https://docs.github.com/organizations/managing-peoples-access-to-your-organization-with-roles/managing-security-managers-in-your-organization). |
| <CopyableCode code="list_alerts_for_org" /> | `SELECT` | <CopyableCode code="org" /> | Lists secret scanning alerts for eligible repositories in an organization, from newest to oldest.<br />To use this endpoint, you must be an administrator or security manager for the organization, and you must use an access token with the `repo` scope or `security_events` scope.<br />For public repositories, you may instead use the `public_repo` scope.<br /><br />GitHub Apps must have the `secret_scanning_alerts` read permission to use this endpoint. |
| <CopyableCode code="list_alerts_for_repo" /> | `SELECT` | <CopyableCode code="owner, repo" /> | Lists secret scanning alerts for an eligible repository, from newest to oldest.<br />To use this endpoint, you must be an administrator for the repository or for the organization that owns the repository, and you must use a personal access token with the `repo` scope or `security_events` scope.<br />For public repositories, you may instead use the `public_repo` scope.<br /><br />GitHub Apps must have the `secret_scanning_alerts` read permission to use this endpoint. |
| <CopyableCode code="update_alert" /> | `EXEC` | <CopyableCode code="alert_number, owner, repo, data__state" /> | Updates the status of a secret scanning alert in an eligible repository.<br />To use this endpoint, you must be an administrator for the repository or for the organization that owns the repository, and you must use a personal access token with the `repo` scope or `security_events` scope.<br />For public repositories, you may instead use the `public_repo` scope.<br /><br />GitHub Apps must have the `secret_scanning_alerts` write permission to use this endpoint. |
