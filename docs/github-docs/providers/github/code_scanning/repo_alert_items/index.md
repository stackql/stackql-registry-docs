---
title: repo_alert_items
hide_title: false
hide_table_of_contents: false
keywords:
  - repo_alert_items
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
<tr><td><b>Name</b></td><td><code>repo_alert_items</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>github.code_scanning.repo_alert_items</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `url` | `string` | The REST API URL of the alert resource. |
| `dismissed_by` | `object` | A GitHub user. |
| `created_at` | `string` | The time that the alert was created in ISO 8601 format: `YYYY-MM-DDTHH:MM:SSZ`. |
| `dismissed_reason` | `string` | **Required when the state is dismissed.** The reason for dismissing or closing the alert. |
| `tool` | `object` |  |
| `dismissed_comment` | `string` | The dismissal comment associated with the dismissal of the alert. |
| `dismissed_at` | `string` | The time that the alert was dismissed in ISO 8601 format: `YYYY-MM-DDTHH:MM:SSZ`. |
| `html_url` | `string` | The GitHub URL of the alert resource. |
| `fixed_at` | `string` | The time that the alert was no longer detected and was considered fixed in ISO 8601 format: `YYYY-MM-DDTHH:MM:SSZ`. |
| `number` | `integer` | The security alert number. |
| `most_recent_instance` | `object` |  |
| `state` | `string` | State of a code scanning alert. |
| `instances_url` | `string` | The REST API URL for fetching the list of instances for an alert. |
| `updated_at` | `string` | The time that the alert was last updated in ISO 8601 format: `YYYY-MM-DDTHH:MM:SSZ`. |
| `rule` | `object` |  |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| `list_alerts_for_repo` | `SELECT` | `owner, repo` |
