---
title: failed_invitations
hide_title: false
hide_table_of_contents: false
keywords:
  - failed_invitations
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
<tr><td><b>Name</b></td><td><code>failed_invitations</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>github.orgs.failed_invitations</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `integer` |  |
| `failed_reason` | `string` |  |
| `inviter` | `object` | Simple User |
| `node_id` | `string` |  |
| `role` | `string` |  |
| `team_count` | `integer` |  |
| `email` | `string` |  |
| `failed_at` | `string` |  |
| `created_at` | `string` |  |
| `invitation_teams_url` | `string` |  |
| `login` | `string` |  |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| `list_failed_invitations` | `SELECT` | `org` |
