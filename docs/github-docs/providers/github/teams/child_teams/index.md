---
title: child_teams
hide_title: false
hide_table_of_contents: false
keywords:
  - child_teams
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
<tr><td><b>Name</b></td><td><code>child_teams</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>github.teams.child_teams</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `integer` |  |
| `name` | `string` |  |
| `description` | `string` |  |
| `parent` | `object` | Groups of organization members that gives permissions on specified repositories. |
| `html_url` | `string` |  |
| `node_id` | `string` |  |
| `repositories_url` | `string` |  |
| `url` | `string` |  |
| `permissions` | `object` |  |
| `members_url` | `string` |  |
| `permission` | `string` |  |
| `slug` | `string` |  |
| `privacy` | `string` |  |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| `list_child_in_org` | `SELECT` | `org, team_slug` |
