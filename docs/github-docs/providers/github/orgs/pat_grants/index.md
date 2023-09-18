---
title: pat_grants
hide_title: false
hide_table_of_contents: false
keywords:
  - pat_grants
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
<tr><td><b>Name</b></td><td><code>pat_grants</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>github.orgs.pat_grants</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `integer` | Unique identifier of the fine-grained personal access token. The `pat_id` used to get details about an approved fine-grained personal access token. |
| `repositories_url` | `string` | URL to the list of repositories the fine-grained personal access token can access. Only follow when `repository_selection` is `subset`. |
| `access_granted_at` | `string` | Date and time when the fine-grained personal access token was approved to access the organization. |
| `owner` | `object` | A GitHub user. |
| `token_expires_at` | `string` | Date and time when the associated fine-grained personal access token expires. |
| `permissions` | `object` | Permissions requested, categorized by type of permission. |
| `token_expired` | `boolean` | Whether the associated fine-grained personal access token has expired. |
| `repository_selection` | `string` | Type of repository selection requested. |
| `token_last_used_at` | `string` | Date and time when the associated fine-grained personal access token was last used for authentication. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `list_pat_grants` | `SELECT` | `org` | Lists approved fine-grained personal access tokens owned by organization members that can access organization resources. Only GitHub Apps can call this API,<br />using the `organization_personal_access_tokens: read` permission.<br /><br />**Note**: Fine-grained PATs are in public beta. Related APIs, events, and functionality are subject to change. |
| `update_pat_access` | `EXEC` | `org, pat_id, data__action` | Updates the access an organization member has to organization resources via a fine-grained personal access token. Limited to revoking the token's existing access. Limited to revoking a token's existing access. Only GitHub Apps can call this API,<br />using the `organization_personal_access_tokens: write` permission.<br /><br />**Note**: Fine-grained PATs are in public beta. Related APIs, events, and functionality are subject to change. |
| `update_pat_accesses` | `EXEC` | `org, data__action, data__pat_ids` | Updates the access organization members have to organization resources via fine-grained personal access tokens. Limited to revoking a token's existing access. Only GitHub Apps can call this API,<br />using the `organization_personal_access_tokens: write` permission.<br /><br />**Note**: Fine-grained PATs are in public beta. Related APIs, events, and functionality are subject to change. |
