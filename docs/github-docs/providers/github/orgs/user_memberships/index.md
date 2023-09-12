---
title: user_memberships
hide_title: false
hide_table_of_contents: false
keywords:
  - user_memberships
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
<tr><td><b>Name</b></td><td><code>user_memberships</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>github.orgs.user_memberships</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `organization_url` | `string` |  |
| `permissions` | `object` |  |
| `role` | `string` | The user's membership type in the organization. |
| `state` | `string` | The state of the member in the organization. The `pending` state indicates the user has not yet accepted an invitation. |
| `url` | `string` |  |
| `user` | `object` | A GitHub user. |
| `organization` | `object` | A GitHub organization. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get_membership_for_authenticated_user` | `SELECT` | `org` | If the authenticated user is an active or pending member of the organization, this endpoint will return the user's membership. If the authenticated user is not affiliated with the organization, a `404` is returned. This endpoint will return a `403` if the request is made by a GitHub App that is blocked by the organization. |
| `list_memberships_for_authenticated_user` | `SELECT` |  | Lists all of the authenticated user's organization memberships. |
| `update_membership_for_authenticated_user` | `EXEC` | `org, data__state` | Converts the authenticated user to an active member of the organization, if that user has a pending invitation from the organization. |
