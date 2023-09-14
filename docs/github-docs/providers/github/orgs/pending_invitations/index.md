---
title: pending_invitations
hide_title: false
hide_table_of_contents: false
keywords:
  - pending_invitations
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
<tr><td><b>Name</b></td><td><code>pending_invitations</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>github.orgs.pending_invitations</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `integer` |  |
| `team_count` | `integer` |  |
| `email` | `string` |  |
| `failed_reason` | `string` |  |
| `invitation_teams_url` | `string` |  |
| `node_id` | `string` |  |
| `created_at` | `string` |  |
| `invitation_source` | `string` |  |
| `role` | `string` |  |
| `login` | `string` |  |
| `failed_at` | `string` |  |
| `inviter` | `object` | A GitHub user. |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| `list_pending_invitations` | `SELECT` | `org` |
