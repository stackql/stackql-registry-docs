---
title: enterprise_alerts
hide_title: false
hide_table_of_contents: false
keywords:
  - enterprise_alerts
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
<tr><td><b>Name</b></td><td><code>enterprise_alerts</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>github.dependabot.enterprise_alerts</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `created_at` | `string` | The time that the alert was created in ISO 8601 format: `YYYY-MM-DDTHH:MM:SSZ`. |
| `dependency` | `object` | Details for the vulnerable dependency. |
| `dismissed_reason` | `string` | The reason that the alert was dismissed. |
| `fixed_at` | `string` | The time that the alert was no longer detected and was considered fixed in ISO 8601 format: `YYYY-MM-DDTHH:MM:SSZ`. |
| `updated_at` | `string` | The time that the alert was last updated in ISO 8601 format: `YYYY-MM-DDTHH:MM:SSZ`. |
| `repository` | `object` | A GitHub repository. |
| `dismissed_by` | `object` | A GitHub user. |
| `dismissed_at` | `string` | The time that the alert was dismissed in ISO 8601 format: `YYYY-MM-DDTHH:MM:SSZ`. |
| `number` | `integer` | The security alert number. |
| `url` | `string` | The REST API URL of the alert resource. |
| `state` | `string` | The state of the Dependabot alert. |
| `security_vulnerability` | `object` | Details pertaining to one vulnerable version range for the advisory. |
| `security_advisory` | `object` | Details for the GitHub Security Advisory. |
| `auto_dismissed_at` | `string` | The time that the alert was auto-dismissed in ISO 8601 format: `YYYY-MM-DDTHH:MM:SSZ`. |
| `dismissed_comment` | `string` | An optional comment associated with the alert's dismissal. |
| `html_url` | `string` | The GitHub URL of the alert resource. |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| `list_alerts_for_enterprise` | `SELECT` | `enterprise` |
