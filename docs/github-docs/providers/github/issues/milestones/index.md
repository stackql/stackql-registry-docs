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
| `node_id` | `string` |  |
| `url` | `string` |  |
| `creator` | `object` | Simple User |
| `closed_at` | `string` |  |
| `state` | `string` | The state of the milestone. |
| `updated_at` | `string` |  |
| `created_at` | `string` |  |
| `closed_issues` | `integer` |  |
| `html_url` | `string` |  |
| `title` | `string` | The title of the milestone. |
| `number` | `integer` | The number of the milestone. |
| `due_on` | `string` |  |
| `open_issues` | `integer` |  |
| `labels_url` | `string` |  |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| `get_milestone` | `SELECT` | `milestone_number, owner, repo` |
| `list_milestones` | `SELECT` | `owner, repo` |
| `create_milestone` | `INSERT` | `owner, repo, data__title` |
| `delete_milestone` | `DELETE` | `milestone_number, owner, repo` |
| `update_milestone` | `EXEC` | `milestone_number, owner, repo` |
