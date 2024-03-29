---
title: teams
hide_title: false
hide_table_of_contents: false
keywords:
  - teams
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
<tr><td><b>Name</b></td><td><code>teams</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>github.repos.teams</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `integer` |  |
| `name` | `string` |  |
| `description` | `string` |  |
| `permission` | `string` |  |
| `privacy` | `string` |  |
| `repositories_url` | `string` |  |
| `node_id` | `string` |  |
| `permissions` | `object` |  |
| `notification_setting` | `string` |  |
| `slug` | `string` |  |
| `html_url` | `string` |  |
| `parent` | `object` | Groups of organization members that gives permissions on specified repositories. |
| `url` | `string` |  |
| `members_url` | `string` |  |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| `list_teams` | `SELECT` | `owner, repo` |
