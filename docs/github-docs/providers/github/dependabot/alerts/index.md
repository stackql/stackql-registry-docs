---
title: alerts
hide_title: false
hide_table_of_contents: false
keywords:
  - alerts
  - dependabot
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
<tr><td><b>Name</b></td><td><code>alerts</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>github.dependabot.alerts</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `updated_at` | `string` | The time that the alert was last updated in ISO 8601 format: `YYYY-MM-DDTHH:MM:SSZ`. |
| `security_vulnerability` | `object` | Details pertaining to one vulnerable version range for the advisory. |
| `dependency` | `object` | Details for the vulnerable dependency. |
| `security_advisory` | `object` | Details for the GitHub Security Advisory. |
| `dismissed_at` | `string` | The time that the alert was dismissed in ISO 8601 format: `YYYY-MM-DDTHH:MM:SSZ`. |
| `fixed_at` | `string` | The time that the alert was no longer detected and was considered fixed in ISO 8601 format: `YYYY-MM-DDTHH:MM:SSZ`. |
| `html_url` | `string` | The GitHub URL of the alert resource. |
| `dismissed_reason` | `string` | The reason that the alert was dismissed. |
| `dismissed_comment` | `string` | An optional comment associated with the alert's dismissal. |
| `dismissed_by` | `object` | A GitHub user. |
| `number` | `integer` | The security alert number. |
| `state` | `string` | The state of the Dependabot alert. |
| `auto_dismissed_at` | `string` | The time that the alert was auto-dismissed in ISO 8601 format: `YYYY-MM-DDTHH:MM:SSZ`. |
| `url` | `string` | The REST API URL of the alert resource. |
| `created_at` | `string` | The time that the alert was created in ISO 8601 format: `YYYY-MM-DDTHH:MM:SSZ`. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get_alert` | `SELECT` | `alert_number, owner, repo` | You must use an access token with the `security_events` scope to use this endpoint with private repositories.<br />You can also use tokens with the `public_repo` scope for public repositories only.<br />GitHub Apps must have **Dependabot alerts** read permission to use this endpoint. |
| `list_alerts_for_repo` | `SELECT` | `owner, repo` | You must use an access token with the `security_events` scope to use this endpoint with private repositories.<br />You can also use tokens with the `public_repo` scope for public repositories only.<br />GitHub Apps must have **Dependabot alerts** read permission to use this endpoint. |
| `update_alert` | `EXEC` | `alert_number, owner, repo, data__state` | You must use an access token with the `security_events` scope to use this endpoint with private repositories.<br />You can also use tokens with the `public_repo` scope for public repositories only.<br />GitHub Apps must have **Dependabot alerts** write permission to use this endpoint.<br /><br />To use this endpoint, you must have access to security alerts for the repository. For more information, see "[Granting access to security alerts](https://docs.github.com/repositories/managing-your-repositorys-settings-and-features/enabling-features-for-your-repository/managing-security-and-analysis-settings-for-your-repository#granting-access-to-security-alerts)." |
