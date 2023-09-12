---
title: enterprises_alerts
hide_title: false
hide_table_of_contents: false
keywords:
  - enterprises_alerts
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
<tr><td><b>Name</b></td><td><code>enterprises_alerts</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>github.secret_scanning.enterprises_alerts</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `url` | `string` | The REST API URL of the alert resource. |
| `push_protection_bypassed_by` | `object` | A GitHub user. |
| `repository` | `object` | A GitHub repository. |
| `secret` | `string` | The secret that was detected. |
| `created_at` | `string` | The time that the alert was created in ISO 8601 format: `YYYY-MM-DDTHH:MM:SSZ`. |
| `locations_url` | `string` | The REST API URL of the code locations for this alert. |
| `html_url` | `string` | The GitHub URL of the alert resource. |
| `number` | `integer` | The security alert number. |
| `state` | `string` | Sets the state of the secret scanning alert. You must provide `resolution` when you set the state to `resolved`. |
| `push_protection_bypassed` | `boolean` | Whether push protection was bypassed for the detected secret. |
| `updated_at` | `string` | The time that the alert was last updated in ISO 8601 format: `YYYY-MM-DDTHH:MM:SSZ`. |
| `push_protection_bypassed_at` | `string` | The time that push protection was bypassed in ISO 8601 format: `YYYY-MM-DDTHH:MM:SSZ`. |
| `resolution_comment` | `string` | The comment that was optionally added when this alert was closed |
| `resolved_at` | `string` | The time that the alert was resolved in ISO 8601 format: `YYYY-MM-DDTHH:MM:SSZ`. |
| `resolved_by` | `object` | A GitHub user. |
| `secret_type` | `string` | The type of secret that secret scanning detected. |
| `resolution` | `string` | **Required when the `state` is `resolved`.** The reason for resolving the alert. |
| `secret_type_display_name` | `string` | User-friendly name for the detected secret, matching the `secret_type`.<br />For a list of built-in patterns, see "[Secret scanning patterns](https://docs.github.com/code-security/secret-scanning/secret-scanning-patterns#supported-secrets-for-advanced-security)." |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| `list_alerts_for_enterprise` | `SELECT` | `enterprise` |
