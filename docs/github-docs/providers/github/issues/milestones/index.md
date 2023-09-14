---
title: milestones
hide_title: false
hide_table_of_contents: false
keywords:
  - milestones
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
<tr><td><b>Name</b></td><td><code>milestones</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>github.issues.milestones</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `integer` |  |
| `description` | `string` |  |
| `open_issues` | `integer` |  |
| `created_at` | `string` |  |
| `due_on` | `string` |  |
| `title` | `string` | The title of the milestone. |
| `creator` | `object` | A GitHub user. |
| `updated_at` | `string` |  |
| `node_id` | `string` |  |
| `state` | `string` | The state of the milestone. |
| `closed_issues` | `integer` |  |
| `html_url` | `string` |  |
| `closed_at` | `string` |  |
| `number` | `integer` | The number of the milestone. |
| `labels_url` | `string` |  |
| `url` | `string` |  |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get_milestone` | `SELECT` | `milestone_number, owner, repo` | Gets a milestone using the given milestone number. |
| `list_milestones` | `SELECT` | `owner, repo` | Lists milestones for a repository. |
| `create_milestone` | `INSERT` | `owner, repo, data__title` | Creates a milestone. |
| `delete_milestone` | `DELETE` | `milestone_number, owner, repo` | Deletes a milestone using the given milestone number. |
| `update_milestone` | `EXEC` | `milestone_number, owner, repo` |  |
