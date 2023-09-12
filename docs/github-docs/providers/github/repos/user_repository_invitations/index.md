---
title: user_repository_invitations
hide_title: false
hide_table_of_contents: false
keywords:
  - user_repository_invitations
  - repos
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
<tr><td><b>Name</b></td><td><code>user_repository_invitations</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>github.repos.user_repository_invitations</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `integer` | Unique identifier of the repository invitation. |
| `repository` | `object` | Minimal Repository |
| `expired` | `boolean` | Whether or not the invitation has expired |
| `html_url` | `string` |  |
| `node_id` | `string` |  |
| `permissions` | `string` | The permission associated with the invitation. |
| `invitee` | `object` | A GitHub user. |
| `inviter` | `object` | A GitHub user. |
| `url` | `string` | URL for the repository invitation |
| `created_at` | `string` |  |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `list_invitations_for_authenticated_user` | `SELECT` |  | When authenticating as a user, this endpoint will list all currently open repository invitations for that user. |
| `accept_invitation_for_authenticated_user` | `EXEC` | `invitation_id` |  |
| `decline_invitation_for_authenticated_user` | `EXEC` | `invitation_id` |  |
