---
title: legacy_child
hide_title: false
hide_table_of_contents: false
keywords:
  - legacy_child
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
<tr><td><b>Name</b></td><td><code>legacy_child</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>github.teams.legacy_child</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `integer` |  |
| `name` | `string` |  |
| `description` | `string` |  |
| `privacy` | `string` |  |
| `members_url` | `string` |  |
| `node_id` | `string` |  |
| `permissions` | `object` |  |
| `repositories_url` | `string` |  |
| `url` | `string` |  |
| `permission` | `string` |  |
| `slug` | `string` |  |
| `html_url` | `string` |  |
| `parent` | `object` | Groups of organization members that gives permissions on specified repositories. |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| `list_child_legacy` | `SELECT` | `team_id` |
