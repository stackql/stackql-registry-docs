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

import CopyableCode from '@site/src/components/CopyableCode/CopyableCode';




## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>pat_grant_requests</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="github.orgs.pat_grant_requests" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `integer` | Unique identifier of the request for access via fine-grained personal access token. The `pat_request_id` used to review PAT requests. |
| <CopyableCode code="created_at" /> | `string` | Date and time when the request for access was created. |
| <CopyableCode code="owner" /> | `object` | A GitHub user. |
| <CopyableCode code="permissions" /> | `object` | Permissions requested, categorized by type of permission. |
| <CopyableCode code="reason" /> | `string` | Reason for requesting access. |
| <CopyableCode code="repositories_url" /> | `string` | URL to the list of repositories requested to be accessed via fine-grained personal access token. Should only be followed when `repository_selection` is `subset`. |
| <CopyableCode code="repository_selection" /> | `string` | Type of repository selection requested. |
| <CopyableCode code="token_expired" /> | `boolean` | Whether the associated fine-grained personal access token has expired. |
| <CopyableCode code="token_expires_at" /> | `string` | Date and time when the associated fine-grained personal access token expires. |
| <CopyableCode code="token_last_used_at" /> | `string` | Date and time when the associated fine-grained personal access token was last used for authentication. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="list_pat_grant_requests" /> | `SELECT` | <CopyableCode code="org" /> | Lists requests from organization members to access organization resources with a fine-grained personal access token. Only GitHub Apps can call this API,<br />using the `organization_personal_access_token_requests: read` permission.<br /><br />**Note**: Fine-grained PATs are in public beta. Related APIs, events, and functionality are subject to change. |
| <CopyableCode code="review_pat_grant_request" /> | `EXEC` | <CopyableCode code="org, pat_request_id, data__action" /> | Approves or denies a pending request to access organization resources via a fine-grained personal access token. Only GitHub Apps can call this API,<br />using the `organization_personal_access_token_requests: write` permission.<br /><br />**Note**: Fine-grained PATs are in public beta. Related APIs, events, and functionality are subject to change. |
| <CopyableCode code="review_pat_grant_requests_in_bulk" /> | `EXEC` | <CopyableCode code="org, data__action" /> | Approves or denies multiple pending requests to access organization resources via a fine-grained personal access token. Only GitHub Apps can call this API,<br />using the `organization_personal_access_token_requests: write` permission.<br /><br />**Note**: Fine-grained PATs are in public beta. Related APIs, events, and functionality are subject to change. |
