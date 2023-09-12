---
title: personal_access_token_requests
hide_title: false
hide_table_of_contents: false
keywords:
  - personal_access_token_requests
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
<tr><td><b>Name</b></td><td><code>personal_access_token_requests</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>github.orgs.personal_access_token_requests</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `integer` | Unique identifier of the request for access via fine-grained personal access token. The `pat_request_id` used to review PAT requests. |
| `repositories_url` | `string` | URL to the list of repositories requested to be accessed via fine-grained personal access token. Should only be followed when `repository_selection` is `subset`. |
| `token_expired` | `boolean` | Whether the associated fine-grained personal access token has expired. |
| `token_expires_at` | `string` | Date and time when the associated fine-grained personal access token expires. |
| `reason` | `string` | Reason for requesting access. |
| `permissions` | `object` | Permissions requested, categorized by type of permission. |
| `repository_selection` | `string` | Type of repository selection requested. |
| `created_at` | `string` | Date and time when the request for access was created. |
| `owner` | `object` | A GitHub user. |
| `token_last_used_at` | `string` | Date and time when the associated fine-grained personal access token was last used for authentication. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `list_pat_grant_requests` | `SELECT` | `org` | Lists requests from organization members to access organization resources with a fine-grained personal access token. Only GitHub Apps can call this API,<br />using the `organization_personal_access_token_requests: read` permission.<br /><br />**Note**: Fine-grained PATs are in public beta. Related APIs, events, and functionality are subject to change. |
| `review_pat_grant_request` | `EXEC` | `org, pat_request_id, data__action` | Approves or denies a pending request to access organization resources via a fine-grained personal access token. Only GitHub Apps can call this API,<br />using the `organization_personal_access_token_requests: write` permission.<br /><br />**Note**: Fine-grained PATs are in public beta. Related APIs, events, and functionality are subject to change. |
| `review_pat_grant_requests_in_bulk` | `EXEC` | `org, data__action` | Approves or denies multiple pending requests to access organization resources via a fine-grained personal access token. Only GitHub Apps can call this API,<br />using the `organization_personal_access_token_requests: write` permission.<br /><br />**Note**: Fine-grained PATs are in public beta. Related APIs, events, and functionality are subject to change. |
