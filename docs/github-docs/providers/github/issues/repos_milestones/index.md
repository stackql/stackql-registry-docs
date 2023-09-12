---
title: repos_milestones
hide_title: false
hide_table_of_contents: false
keywords:
  - repos_milestones
  - issues
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
<tr><td><b>Name</b></td><td><code>repos_milestones</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>github.issues.repos_milestones</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `integer` |  |
| `description` | `string` |  |
| `open_issues` | `integer` |  |
| `node_id` | `string` |  |
| `number` | `integer` | The number of the milestone. |
| `html_url` | `string` |  |
| `labels_url` | `string` |  |
| `created_at` | `string` |  |
| `url` | `string` |  |
| `state` | `string` | The state of the milestone. |
| `due_on` | `string` |  |
| `closed_at` | `string` |  |
| `closed_issues` | `integer` |  |
| `creator` | `object` | A GitHub user. |
| `updated_at` | `string` |  |
| `title` | `string` | The title of the milestone. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get_milestone` | `SELECT` | `milestone_number, owner, repo` | Gets a milestone using the given milestone number. |
| `list_milestones` | `SELECT` | `owner, repo` | Lists milestones for a repository. |
| `create_milestone` | `INSERT` | `owner, repo, data__title` | Creates a milestone. |
| `delete_milestone` | `DELETE` | `milestone_number, owner, repo` | Deletes a milestone using the given milestone number. |
| `update_milestone` | `EXEC` | `milestone_number, owner, repo` |  |
