---
title: repos_labels
hide_title: false
hide_table_of_contents: false
keywords:
  - repos_labels
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
<tr><td><b>Name</b></td><td><code>repos_labels</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>github.issues.repos_labels</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `integer` |  |
| `name` | `string` | The name of the label. |
| `description` | `string` |  |
| `node_id` | `string` |  |
| `url` | `string` | URL for the label |
| `color` | `string` | 6-character hex code, without the leading #, identifying the color |
| `default` | `boolean` |  |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get_label` | `SELECT` | `name, owner, repo` | Gets a label using the given name. |
| `list_labels_for_repo` | `SELECT` | `owner, repo` | Lists all labels for a repository. |
| `list_labels_on_issue` | `SELECT` | `issue_number, owner, repo` | Lists all labels for an issue. |
| `add_labels` | `INSERT` | `issue_number, owner, repo` | Adds labels to an issue. If you provide an empty array of labels, all labels are removed from the issue.  |
| `create_label` | `INSERT` | `owner, repo, data__name` | Creates a label for the specified repository with the given name and color. The name and color parameters are required. The color must be a valid [hexadecimal color code](http://www.color-hex.com/). |
| `delete_label` | `DELETE` | `name, owner, repo` | Deletes a label using the given label name. |
| `remove_all_labels` | `DELETE` | `issue_number, owner, repo` | Removes all labels from an issue. |
| `remove_label` | `DELETE` | `issue_number, name, owner, repo` | Removes the specified label from the issue, and returns the remaining labels on the issue. This endpoint returns a `404 Not Found` status if the label does not exist. |
| `set_labels` | `EXEC` | `issue_number, owner, repo` | Removes any previous labels and sets the new labels for an issue. |
| `update_label` | `EXEC` | `name, owner, repo` | Updates a label using the given label name. |
