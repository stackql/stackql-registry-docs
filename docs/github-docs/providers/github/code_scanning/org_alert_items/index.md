---
title: org_alert_items
hide_title: false
hide_table_of_contents: false
keywords:
  - org_alert_items
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
<tr><td><b>Name</b></td><td><code>org_alert_items</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>github.code_scanning.org_alert_items</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `updated_at` | `string` | The time that the alert was last updated in ISO 8601 format: `YYYY-MM-DDTHH:MM:SSZ`. |
| `dismissed_reason` | `string` | **Required when the state is dismissed.** The reason for dismissing or closing the alert. |
| `number` | `integer` | The security alert number. |
| `dismissed_at` | `string` | The time that the alert was dismissed in ISO 8601 format: `YYYY-MM-DDTHH:MM:SSZ`. |
| `tool` | `object` |  |
| `instances_url` | `string` | The REST API URL for fetching the list of instances for an alert. |
| `rule` | `object` |  |
| `state` | `string` | State of a code scanning alert. |
| `most_recent_instance` | `object` |  |
| `fixed_at` | `string` | The time that the alert was no longer detected and was considered fixed in ISO 8601 format: `YYYY-MM-DDTHH:MM:SSZ`. |
| `repository` | `object` | A GitHub repository. |
| `dismissed_comment` | `string` | The dismissal comment associated with the dismissal of the alert. |
| `created_at` | `string` | The time that the alert was created in ISO 8601 format: `YYYY-MM-DDTHH:MM:SSZ`. |
| `html_url` | `string` | The GitHub URL of the alert resource. |
| `url` | `string` | The REST API URL of the alert resource. |
| `dismissed_by` | `object` | A GitHub user. |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| `list_alerts_for_org` | `SELECT` | `org` |
