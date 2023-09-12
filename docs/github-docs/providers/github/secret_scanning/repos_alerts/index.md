---
title: repos_alerts
hide_title: false
hide_table_of_contents: false
keywords:
  - repos_alerts
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
  
    

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>repos_alerts</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>github.secret_scanning.repos_alerts</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `secret_type_display_name` | `string` | User-friendly name for the detected secret, matching the `secret_type`.<br />For a list of built-in patterns, see "[Secret scanning patterns](https://docs.github.com/code-security/secret-scanning/secret-scanning-patterns#supported-secrets-for-advanced-security)." |
| `state` | `string` | Sets the state of the secret scanning alert. You must provide `resolution` when you set the state to `resolved`. |
| `resolved_at` | `string` | The time that the alert was resolved in ISO 8601 format: `YYYY-MM-DDTHH:MM:SSZ`. |
| `html_url` | `string` | The GitHub URL of the alert resource. |
| `push_protection_bypassed_at` | `string` | The time that push protection was bypassed in ISO 8601 format: `YYYY-MM-DDTHH:MM:SSZ`. |
| `updated_at` | `string` | The time that the alert was last updated in ISO 8601 format: `YYYY-MM-DDTHH:MM:SSZ`. |
| `push_protection_bypassed_by` | `object` | A GitHub user. |
| `resolution` | `string` | **Required when the `state` is `resolved`.** The reason for resolving the alert. |
| `resolution_comment` | `string` | An optional comment to resolve an alert. |
| `url` | `string` | The REST API URL of the alert resource. |
| `locations_url` | `string` | The REST API URL of the code locations for this alert. |
| `created_at` | `string` | The time that the alert was created in ISO 8601 format: `YYYY-MM-DDTHH:MM:SSZ`. |
| `number` | `integer` | The security alert number. |
| `secret` | `string` | The secret that was detected. |
| `push_protection_bypassed` | `boolean` | Whether push protection was bypassed for the detected secret. |
| `resolved_by` | `object` | A GitHub user. |
| `secret_type` | `string` | The type of secret that secret scanning detected. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get_alert` | `SELECT` | `alert_number, owner, repo` | Gets a single secret scanning alert detected in an eligible repository.<br />To use this endpoint, you must be an administrator for the repository or for the organization that owns the repository, and you must use a personal access token with the `repo` scope or `security_events` scope.<br />For public repositories, you may instead use the `public_repo` scope.<br /><br />GitHub Apps must have the `secret_scanning_alerts` read permission to use this endpoint. |
| `list_alerts_for_repo` | `SELECT` | `owner, repo` | Lists secret scanning alerts for an eligible repository, from newest to oldest.<br />To use this endpoint, you must be an administrator for the repository or for the organization that owns the repository, and you must use a personal access token with the `repo` scope or `security_events` scope.<br />For public repositories, you may instead use the `public_repo` scope.<br /><br />GitHub Apps must have the `secret_scanning_alerts` read permission to use this endpoint. |
| `update_alert` | `EXEC` | `alert_number, owner, repo, data__state` | Updates the status of a secret scanning alert in an eligible repository.<br />To use this endpoint, you must be an administrator for the repository or for the organization that owns the repository, and you must use a personal access token with the `repo` scope or `security_events` scope.<br />For public repositories, you may instead use the `public_repo` scope.<br /><br />GitHub Apps must have the `secret_scanning_alerts` write permission to use this endpoint. |
