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

import CopyableCode from '@site/src/components/CopyableCode/CopyableCode';




## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>columns</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="github.projects.columns" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `integer` | The unique identifier of the project column |
| <CopyableCode code="name" /> | `string` | Name of the project column |
| <CopyableCode code="cards_url" /> | `string` |  |
| <CopyableCode code="created_at" /> | `string` |  |
| <CopyableCode code="node_id" /> | `string` |  |
| <CopyableCode code="project_url" /> | `string` |  |
| <CopyableCode code="updated_at" /> | `string` |  |
| <CopyableCode code="url" /> | `string` |  |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get_column" /> | `SELECT` | <CopyableCode code="column_id" /> | Gets information about a project column. |
| <CopyableCode code="list_columns" /> | `SELECT` | <CopyableCode code="project_id" /> | Lists the project columns in a project. |
| <CopyableCode code="create_column" /> | `INSERT` | <CopyableCode code="project_id, data__name" /> | Creates a new project column. |
| <CopyableCode code="delete_column" /> | `DELETE` | <CopyableCode code="column_id" /> | Deletes a project column. |
| <CopyableCode code="move_column" /> | `EXEC` | <CopyableCode code="column_id, data__position" /> |  |
| <CopyableCode code="update_column" /> | `EXEC` | <CopyableCode code="column_id, data__name" /> |  |
