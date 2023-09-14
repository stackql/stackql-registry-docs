---
title: invitation_teams
hide_title: false
hide_table_of_contents: false
keywords:
  - invitation_teams
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
<tr><td><b>Name</b></td><td><code>invitation_teams</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>github.orgs.invitation_teams</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `integer` |  |
| `name` | `string` |  |
| `description` | `string` |  |
| `members_url` | `string` |  |
| `slug` | `string` |  |
| `html_url` | `string` |  |
| `parent` | `object` | Groups of organization members that gives permissions on specified repositories. |
| `permission` | `string` |  |
| `node_id` | `string` |  |
| `notification_setting` | `string` |  |
| `privacy` | `string` |  |
| `repositories_url` | `string` |  |
| `permissions` | `object` |  |
| `url` | `string` |  |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| `list_invitation_teams` | `SELECT` | `invitation_id, org` |
