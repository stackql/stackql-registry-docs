---
title: labels
hide_title: false
hide_table_of_contents: false
keywords:
  - labels
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

import CopyableCode from '@site/src/components/CopyableCode/CopyableCode';




## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>labels</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="github.issues.labels" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `integer` |  |
| <CopyableCode code="name" /> | `string` | The name of the label. |
| <CopyableCode code="description" /> | `string` |  |
| <CopyableCode code="color" /> | `string` | 6-character hex code, without the leading #, identifying the color |
| <CopyableCode code="default" /> | `boolean` |  |
| <CopyableCode code="node_id" /> | `string` |  |
| <CopyableCode code="url" /> | `string` | URL for the label |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get_label" /> | `SELECT` | <CopyableCode code="name, owner, repo" /> | Gets a label using the given name. |
| <CopyableCode code="list_labels_for_milestone" /> | `SELECT` | <CopyableCode code="milestone_number, owner, repo" /> | Lists labels for issues in a milestone. |
| <CopyableCode code="list_labels_for_repo" /> | `SELECT` | <CopyableCode code="owner, repo" /> | Lists all labels for a repository. |
| <CopyableCode code="list_labels_on_issue" /> | `SELECT` | <CopyableCode code="issue_number, owner, repo" /> | Lists all labels for an issue. |
| <CopyableCode code="add_labels" /> | `INSERT` | <CopyableCode code="issue_number, owner, repo" /> | Adds labels to an issue. If you provide an empty array of labels, all labels are removed from the issue.  |
| <CopyableCode code="create_label" /> | `INSERT` | <CopyableCode code="owner, repo, data__name" /> | Creates a label for the specified repository with the given name and color. The name and color parameters are required. The color must be a valid [hexadecimal color code](http://www.color-hex.com/). |
| <CopyableCode code="delete_label" /> | `DELETE` | <CopyableCode code="name, owner, repo" /> | Deletes a label using the given label name. |
| <CopyableCode code="remove_all_labels" /> | `DELETE` | <CopyableCode code="issue_number, owner, repo" /> | Removes all labels from an issue. |
| <CopyableCode code="remove_label" /> | `DELETE` | <CopyableCode code="issue_number, name, owner, repo" /> | Removes the specified label from the issue, and returns the remaining labels on the issue. This endpoint returns a `404 Not Found` status if the label does not exist. |
| <CopyableCode code="set_labels" /> | `EXEC` | <CopyableCode code="issue_number, owner, repo" /> | Removes any previous labels and sets the new labels for an issue. |
| <CopyableCode code="update_label" /> | `EXEC` | <CopyableCode code="name, owner, repo" /> | Updates a label using the given label name. |
