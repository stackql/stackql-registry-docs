---
title: columns_cards
hide_title: false
hide_table_of_contents: false
keywords:
  - columns_cards
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
<tr><td><b>Name</b></td><td><code>columns_cards</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>github.projects.columns_cards</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `integer` | The project card's ID |
| `updated_at` | `string` |  |
| `project_url` | `string` |  |
| `node_id` | `string` |  |
| `content_url` | `string` |  |
| `column_url` | `string` |  |
| `column_name` | `string` |  |
| `url` | `string` |  |
| `created_at` | `string` |  |
| `project_id` | `string` |  |
| `creator` | `object` | A GitHub user. |
| `archived` | `boolean` | Whether or not the card is archived |
| `note` | `string` |  |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get_card` | `SELECT` | `card_id` | Gets information about a project card. |
| `list_cards` | `SELECT` | `column_id` | Lists the project cards in a project. |
| `create_card` | `INSERT` | `column_id` |  |
| `delete_card` | `DELETE` | `card_id` | Deletes a project card |
| `move_card` | `EXEC` | `card_id, data__position` |  |
| `update_card` | `EXEC` | `card_id` |  |
