---
title: invitations
hide_title: false
hide_table_of_contents: false
keywords:
  - invitations
  - teams
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
<tr><td><b>Id</b></td><td><code>github.teams.invitations</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `integer` |  |
| `created_at` | `string` |  |
| `role` | `string` |  |
| `invitation_teams_url` | `string` |  |
| `inviter` | `object` | A GitHub user. |
| `login` | `string` |  |
| `team_count` | `integer` |  |
| `email` | `string` |  |
| `failed_at` | `string` |  |
| `node_id` | `string` |  |
| `failed_reason` | `string` |  |
| `invitation_source` | `string` |  |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| `list_pending_invitations_legacy` | `SELECT` | `team_id` |
