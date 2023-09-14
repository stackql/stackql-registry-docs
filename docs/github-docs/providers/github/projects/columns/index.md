---
title: columns
hide_title: false
hide_table_of_contents: false
keywords:
  - columns
  - projects
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
<tr><td><b>Name</b></td><td><code>columns</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>github.projects.columns</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `integer` | The unique identifier of the project column |
| `name` | `string` | Name of the project column |
| `created_at` | `string` |  |
| `node_id` | `string` |  |
| `project_url` | `string` |  |
| `updated_at` | `string` |  |
| `url` | `string` |  |
| `cards_url` | `string` |  |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get_column` | `SELECT` | `column_id` | Gets information about a project column. |
| `list_columns` | `SELECT` | `project_id` | Lists the project columns in a project. |
| `create_column` | `INSERT` | `project_id, data__name` | Creates a new project column. |
| `delete_column` | `DELETE` | `column_id` | Deletes a project column. |
| `move_column` | `EXEC` | `column_id, data__position` |  |
| `update_column` | `EXEC` | `column_id, data__name` |  |
