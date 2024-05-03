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

import CopyableCode from '@site/src/components/CopyableCode/CopyableCode';




## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>cards</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="github.projects.cards" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `integer` | The project card's ID |
| <CopyableCode code="archived" /> | `boolean` | Whether or not the card is archived |
| <CopyableCode code="column_name" /> | `string` |  |
| <CopyableCode code="column_url" /> | `string` |  |
| <CopyableCode code="content_url" /> | `string` |  |
| <CopyableCode code="created_at" /> | `string` |  |
| <CopyableCode code="creator" /> | `object` | A GitHub user. |
| <CopyableCode code="node_id" /> | `string` |  |
| <CopyableCode code="note" /> | `string` |  |
| <CopyableCode code="project_id" /> | `string` |  |
| <CopyableCode code="project_url" /> | `string` |  |
| <CopyableCode code="updated_at" /> | `string` |  |
| <CopyableCode code="url" /> | `string` |  |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get_card" /> | `SELECT` | <CopyableCode code="card_id" /> | Gets information about a project card. |
| <CopyableCode code="list_cards" /> | `SELECT` | <CopyableCode code="column_id" /> | Lists the project cards in a project. |
| <CopyableCode code="create_card" /> | `INSERT` | <CopyableCode code="column_id" /> |  |
| <CopyableCode code="delete_card" /> | `DELETE` | <CopyableCode code="card_id" /> | Deletes a project card |
| <CopyableCode code="move_card" /> | `EXEC` | <CopyableCode code="card_id, data__position" /> |  |
| <CopyableCode code="update_card" /> | `EXEC` | <CopyableCode code="card_id" /> |  |
