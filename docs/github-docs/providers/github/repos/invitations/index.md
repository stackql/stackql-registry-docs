---
title: invitations
hide_title: false
hide_table_of_contents: false
keywords:
  - invitations
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
<tr><td><b>Name</b></td><td><code>invitations</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>github.repos.invitations</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `integer` | Unique identifier of the repository invitation. |
| `repository` | `object` | Minimal Repository |
| `inviter` | `object` | Simple User |
| `html_url` | `string` |  |
| `node_id` | `string` |  |
| `url` | `string` | URL for the repository invitation |
| `created_at` | `string` |  |
| `permissions` | `string` | The permission associated with the invitation. |
| `expired` | `boolean` | Whether or not the invitation has expired |
| `invitee` | `object` | Simple User |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `list_invitations` | `SELECT` | `owner, repo` | When authenticating as a user with admin rights to a repository, this endpoint will list all currently open repository invitations. |
| `list_invitations_for_authenticated_user` | `SELECT` |  | When authenticating as a user, this endpoint will list all currently open repository invitations for that user. |
| `delete_invitation` | `DELETE` | `invitation_id, owner, repo` |  |
| `accept_invitation_for_authenticated_user` | `EXEC` | `invitation_id` |  |
| `decline_invitation_for_authenticated_user` | `EXEC` | `invitation_id` |  |
| `update_invitation` | `EXEC` | `invitation_id, owner, repo` |  |
