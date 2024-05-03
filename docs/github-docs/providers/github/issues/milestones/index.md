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

import CopyableCode from '@site/src/components/CopyableCode/CopyableCode';




## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>milestones</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="github.issues.milestones" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `integer` |  |
| <CopyableCode code="description" /> | `string` |  |
| <CopyableCode code="closed_at" /> | `string` |  |
| <CopyableCode code="closed_issues" /> | `integer` |  |
| <CopyableCode code="created_at" /> | `string` |  |
| <CopyableCode code="creator" /> | `object` | A GitHub user. |
| <CopyableCode code="due_on" /> | `string` |  |
| <CopyableCode code="html_url" /> | `string` |  |
| <CopyableCode code="labels_url" /> | `string` |  |
| <CopyableCode code="node_id" /> | `string` |  |
| <CopyableCode code="number" /> | `integer` | The number of the milestone. |
| <CopyableCode code="open_issues" /> | `integer` |  |
| <CopyableCode code="state" /> | `string` | The state of the milestone. |
| <CopyableCode code="title" /> | `string` | The title of the milestone. |
| <CopyableCode code="updated_at" /> | `string` |  |
| <CopyableCode code="url" /> | `string` |  |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get_milestone" /> | `SELECT` | <CopyableCode code="milestone_number, owner, repo" /> | Gets a milestone using the given milestone number. |
| <CopyableCode code="list_milestones" /> | `SELECT` | <CopyableCode code="owner, repo" /> | Lists milestones for a repository. |
| <CopyableCode code="create_milestone" /> | `INSERT` | <CopyableCode code="owner, repo, data__title" /> | Creates a milestone. |
| <CopyableCode code="delete_milestone" /> | `DELETE` | <CopyableCode code="milestone_number, owner, repo" /> | Deletes a milestone using the given milestone number. |
| <CopyableCode code="update_milestone" /> | `EXEC` | <CopyableCode code="milestone_number, owner, repo" /> |  |
