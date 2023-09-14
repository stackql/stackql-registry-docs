---
title: pat_grant_requests
hide_title: false
hide_table_of_contents: false
keywords:
  - pat_grant_requests
  - orgs
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
<tr><td><b>Name</b></td><td><code>pat_grant_requests</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>github.orgs.pat_grant_requests</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `integer` | Unique identifier of the request for access via fine-grained personal access token. The `pat_request_id` used to review PAT requests. |
| `repository_selection` | `string` | Type of repository selection requested. |
| `permissions` | `object` | Permissions requested, categorized by type of permission. |
| `created_at` | `string` | Date and time when the request for access was created. |
| `owner` | `object` | A GitHub user. |
| `token_expired` | `boolean` | Whether the associated fine-grained personal access token has expired. |
| `token_last_used_at` | `string` | Date and time when the associated fine-grained personal access token was last used for authentication. |
| `token_expires_at` | `string` | Date and time when the associated fine-grained personal access token expires. |
| `reason` | `string` | Reason for requesting access. |
| `repositories_url` | `string` | URL to the list of repositories requested to be accessed via fine-grained personal access token. Should only be followed when `repository_selection` is `subset`. |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| `list_pat_grant_requests` | `SELECT` | `org` |
