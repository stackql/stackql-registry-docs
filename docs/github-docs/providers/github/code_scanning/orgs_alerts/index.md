---
title: orgs_alerts
hide_title: false
hide_table_of_contents: false
keywords:
  - orgs_alerts
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
<tr><td><b>Name</b></td><td><code>orgs_alerts</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>github.code_scanning.orgs_alerts</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `state` | `string` | State of a code scanning alert. |
| `rule` | `object` |  |
| `most_recent_instance` | `object` |  |
| `instances_url` | `string` | The REST API URL for fetching the list of instances for an alert. |
| `dismissed_comment` | `string` | The dismissal comment associated with the dismissal of the alert. |
| `fixed_at` | `string` | The time that the alert was no longer detected and was considered fixed in ISO 8601 format: `YYYY-MM-DDTHH:MM:SSZ`. |
| `dismissed_by` | `object` | A GitHub user. |
| `repository` | `object` | A GitHub repository. |
| `tool` | `object` |  |
| `dismissed_reason` | `string` | **Required when the state is dismissed.** The reason for dismissing or closing the alert. |
| `updated_at` | `string` | The time that the alert was last updated in ISO 8601 format: `YYYY-MM-DDTHH:MM:SSZ`. |
| `url` | `string` | The REST API URL of the alert resource. |
| `number` | `integer` | The security alert number. |
| `dismissed_at` | `string` | The time that the alert was dismissed in ISO 8601 format: `YYYY-MM-DDTHH:MM:SSZ`. |
| `created_at` | `string` | The time that the alert was created in ISO 8601 format: `YYYY-MM-DDTHH:MM:SSZ`. |
| `html_url` | `string` | The GitHub URL of the alert resource. |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| `list_alerts_for_org` | `SELECT` | `org` |
