---
title: labels
hide_title: false
hide_table_of_contents: false
keywords:
  - stackql
  - github
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage GitHub resources using SQL
custom_edit_url: null
image: https://storage.googleapis.com/stackql-web-assets/blog/stackql-blog-post-featured-image.png
---
  
    

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>labels</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>github.issues.labels</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `integer` |  |
| `name` | `string` | The name of the label. |
| `description` | `string` |  |
| `default` | `boolean` |  |
| `node_id` | `string` |  |
| `url` | `string` | URL for the label |
| `color` | `string` | 6-character hex code, without the leading #, identifying the color |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get_label` | `SELECT` | `name, owner, repo` |  |
| `list_labels_for_milestone` | `SELECT` | `milestone_number, owner, repo` |  |
| `list_labels_for_repo` | `SELECT` | `owner, repo` |  |
| `list_labels_on_issue` | `SELECT` | `issue_number, owner, repo` |  |
| `add_labels` | `INSERT` | `issue_number, owner, repo` |  |
| `create_label` | `INSERT` | `owner, repo, data__name` |  |
| `delete_label` | `DELETE` | `name, owner, repo` |  |
| `remove_all_labels` | `DELETE` | `issue_number, owner, repo` |  |
| `remove_label` | `DELETE` | `issue_number, name, owner, repo` | Removes the specified label from the issue, and returns the remaining labels on the issue. This endpoint returns a `404 Not Found` status if the label does not exist. |
| `set_labels` | `EXEC` | `issue_number, owner, repo` | Removes any previous labels and sets the new labels for an issue. |
| `update_label` | `EXEC` | `name, owner, repo` |  |
