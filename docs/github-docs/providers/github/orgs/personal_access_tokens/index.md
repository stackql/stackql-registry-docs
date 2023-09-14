---
title: personal_access_tokens
hide_title: false
hide_table_of_contents: false
keywords:
  - personal_access_tokens
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
<tr><td><b>Name</b></td><td><code>personal_access_tokens</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>github.orgs.personal_access_tokens</code></td></tr>
</tbody></table>

## Fields
`SELECT` not supported for this resource, use `SHOW METHODS` to view available operations for the resource and then invoke a supported method using the `EXEC` command  
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `review_pat_grant_request` | `EXEC` | `org, pat_request_id, data__action` | Approves or denies a pending request to access organization resources via a fine-grained personal access token. Only GitHub Apps can call this API,<br />using the `organization_personal_access_token_requests: write` permission.<br /><br />**Note**: Fine-grained PATs are in public beta. Related APIs, events, and functionality are subject to change. |
| `review_pat_grant_requests_in_bulk` | `EXEC` | `org, data__action` | Approves or denies multiple pending requests to access organization resources via a fine-grained personal access token. Only GitHub Apps can call this API,<br />using the `organization_personal_access_token_requests: write` permission.<br /><br />**Note**: Fine-grained PATs are in public beta. Related APIs, events, and functionality are subject to change. |
| `update_pat_access` | `EXEC` | `org, pat_id, data__action` | Updates the access an organization member has to organization resources via a fine-grained personal access token. Limited to revoking the token's existing access. Limited to revoking a token's existing access. Only GitHub Apps can call this API,<br />using the `organization_personal_access_tokens: write` permission.<br /><br />**Note**: Fine-grained PATs are in public beta. Related APIs, events, and functionality are subject to change. |
| `update_pat_accesses` | `EXEC` | `org, data__action, data__pat_ids` | Updates the access organization members have to organization resources via fine-grained personal access tokens. Limited to revoking a token's existing access. Only GitHub Apps can call this API,<br />using the `organization_personal_access_tokens: write` permission.<br /><br />**Note**: Fine-grained PATs are in public beta. Related APIs, events, and functionality are subject to change. |
