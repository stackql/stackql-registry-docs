---
title: orgs_invitations
hide_title: false
hide_table_of_contents: false
keywords:
  - orgs_invitations
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
<tr><td><b>Name</b></td><td><code>orgs_invitations</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>github.teams.orgs_invitations</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `integer` |  |
| `role` | `string` |  |
| `email` | `string` |  |
| `failed_reason` | `string` |  |
| `inviter` | `object` | A GitHub user. |
| `invitation_source` | `string` |  |
| `invitation_teams_url` | `string` |  |
| `node_id` | `string` |  |
| `created_at` | `string` |  |
| `failed_at` | `string` |  |
| `login` | `string` |  |
| `team_count` | `integer` |  |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| `list_pending_invitations_in_org` | `SELECT` | `org, team_slug` |
