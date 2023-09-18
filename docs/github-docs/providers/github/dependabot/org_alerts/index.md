---
title: org_alerts
hide_title: false
hide_table_of_contents: false
keywords:
  - org_alerts
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
<tr><td><b>Name</b></td><td><code>org_alerts</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>github.dependabot.org_alerts</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `dismissed_reason` | `string` | The reason that the alert was dismissed. |
| `auto_dismissed_at` | `string` | The time that the alert was auto-dismissed in ISO 8601 format: `YYYY-MM-DDTHH:MM:SSZ`. |
| `dismissed_by` | `object` | A GitHub user. |
| `dismissed_comment` | `string` | An optional comment associated with the alert's dismissal. |
| `dependency` | `object` | Details for the vulnerable dependency. |
| `security_advisory` | `object` | Details for the GitHub Security Advisory. |
| `updated_at` | `string` | The time that the alert was last updated in ISO 8601 format: `YYYY-MM-DDTHH:MM:SSZ`. |
| `html_url` | `string` | The GitHub URL of the alert resource. |
| `fixed_at` | `string` | The time that the alert was no longer detected and was considered fixed in ISO 8601 format: `YYYY-MM-DDTHH:MM:SSZ`. |
| `repository` | `object` | A GitHub repository. |
| `url` | `string` | The REST API URL of the alert resource. |
| `state` | `string` | The state of the Dependabot alert. |
| `security_vulnerability` | `object` | Details pertaining to one vulnerable version range for the advisory. |
| `created_at` | `string` | The time that the alert was created in ISO 8601 format: `YYYY-MM-DDTHH:MM:SSZ`. |
| `dismissed_at` | `string` | The time that the alert was dismissed in ISO 8601 format: `YYYY-MM-DDTHH:MM:SSZ`. |
| `number` | `integer` | The security alert number. |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| `list_alerts_for_org` | `SELECT` | `org` |
