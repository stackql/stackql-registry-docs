---
title: cards
hide_title: false
hide_table_of_contents: false
keywords:
  - cards
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
<tr><td><b>Name</b></td><td><code>cards</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>github.projects.cards</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `integer` | The project card's ID |
| `node_id` | `string` |  |
| `column_url` | `string` |  |
| `creator` | `object` | Simple User |
| `url` | `string` |  |
| `content_url` | `string` |  |
| `project_id` | `string` |  |
| `created_at` | `string` |  |
| `project_url` | `string` |  |
| `column_name` | `string` |  |
| `archived` | `boolean` | Whether or not the card is archived |
| `updated_at` | `string` |  |
| `note` | `string` |  |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| `get_card` | `SELECT` | `card_id` |
| `list_cards` | `SELECT` | `column_id` |
| `create_card` | `INSERT` | `column_id` |
| `delete_card` | `DELETE` | `card_id` |
| `move_card` | `EXEC` | `card_id, data__position` |
| `update_card` | `EXEC` | `card_id` |
