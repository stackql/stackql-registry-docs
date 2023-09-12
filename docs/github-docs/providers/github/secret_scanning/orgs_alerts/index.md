---
title: orgs_alerts
hide_title: false
hide_table_of_contents: false
keywords:
  - orgs_alerts
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
<tr><td><b>Name</b></td><td><code>orgs_alerts</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>github.secret_scanning.orgs_alerts</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `html_url` | `string` | The GitHub URL of the alert resource. |
| `repository` | `object` | A GitHub repository. |
| `number` | `integer` | The security alert number. |
| `locations_url` | `string` | The REST API URL of the code locations for this alert. |
| `resolution` | `string` | **Required when the `state` is `resolved`.** The reason for resolving the alert. |
| `secret_type` | `string` | The type of secret that secret scanning detected. |
| `resolved_at` | `string` | The time that the alert was resolved in ISO 8601 format: `YYYY-MM-DDTHH:MM:SSZ`. |
| `created_at` | `string` | The time that the alert was created in ISO 8601 format: `YYYY-MM-DDTHH:MM:SSZ`. |
| `push_protection_bypassed` | `boolean` | Whether push protection was bypassed for the detected secret. |
| `secret_type_display_name` | `string` | User-friendly name for the detected secret, matching the `secret_type`.<br />For a list of built-in patterns, see "[Secret scanning patterns](https://docs.github.com/code-security/secret-scanning/secret-scanning-patterns#supported-secrets-for-advanced-security)." |
| `resolved_by` | `object` | A GitHub user. |
| `push_protection_bypassed_at` | `string` | The time that push protection was bypassed in ISO 8601 format: `YYYY-MM-DDTHH:MM:SSZ`. |
| `resolution_comment` | `string` | The comment that was optionally added when this alert was closed |
| `url` | `string` | The REST API URL of the alert resource. |
| `updated_at` | `string` | The time that the alert was last updated in ISO 8601 format: `YYYY-MM-DDTHH:MM:SSZ`. |
| `secret` | `string` | The secret that was detected. |
| `push_protection_bypassed_by` | `object` | A GitHub user. |
| `state` | `string` | Sets the state of the secret scanning alert. You must provide `resolution` when you set the state to `resolved`. |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| `list_alerts_for_org` | `SELECT` | `org` |
