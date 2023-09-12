---
title: repos_alerts
hide_title: false
hide_table_of_contents: false
keywords:
  - repos_alerts
  - code_scanning
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
<tr><td><b>Id</b></td><td><code>github.code_scanning.repos_alerts</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `state` | `string` | State of a code scanning alert. |
| `tool` | `object` |  |
| `dismissed_at` | `string` | The time that the alert was dismissed in ISO 8601 format: `YYYY-MM-DDTHH:MM:SSZ`. |
| `url` | `string` | The REST API URL of the alert resource. |
| `most_recent_instance` | `object` |  |
| `updated_at` | `string` | The time that the alert was last updated in ISO 8601 format: `YYYY-MM-DDTHH:MM:SSZ`. |
| `number` | `integer` | The security alert number. |
| `rule` | `object` |  |
| `fixed_at` | `string` | The time that the alert was no longer detected and was considered fixed in ISO 8601 format: `YYYY-MM-DDTHH:MM:SSZ`. |
| `created_at` | `string` | The time that the alert was created in ISO 8601 format: `YYYY-MM-DDTHH:MM:SSZ`. |
| `instances_url` | `string` | The REST API URL for fetching the list of instances for an alert. |
| `dismissed_comment` | `string` | The dismissal comment associated with the dismissal of the alert. |
| `html_url` | `string` | The GitHub URL of the alert resource. |
| `dismissed_by` | `object` | A GitHub user. |
| `dismissed_reason` | `string` | **Required when the state is dismissed.** The reason for dismissing or closing the alert. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get_alert` | `SELECT` | `alert_number, owner, repo` | Gets a single code scanning alert. You must use an access token with the `security_events` scope to use this endpoint with private repos, the `public_repo` scope also grants permission to read security events on public repos only. GitHub Apps must have the `security_events` read permission to use this endpoint. |
| `list_alerts_for_repo` | `SELECT` | `owner, repo` | Lists code scanning alerts.<br /><br />To use this endpoint, you must use an access token with the `security_events` scope or, for alerts from public repositories only, an access token with the `public_repo` scope.<br /><br />GitHub Apps must have the `security_events` read<br />permission to use this endpoint.<br /><br />The response includes a `most_recent_instance` object.<br />This provides details of the most recent instance of this alert<br />for the default branch (or for the specified Git reference if you used `ref` in the request). |
| `update_alert` | `EXEC` | `alert_number, owner, repo, data__state` | Updates the status of a single code scanning alert. You must use an access token with the `security_events` scope to use this endpoint with private repositories. You can also use tokens with the `public_repo` scope for public repositories only. GitHub Apps must have the `security_events` write permission to use this endpoint. |
