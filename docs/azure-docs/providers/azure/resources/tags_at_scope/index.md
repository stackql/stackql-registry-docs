---
title: tags_at_scope
hide_title: false
hide_table_of_contents: false
keywords:
  - tags_at_scope
  - resources
  - azure    
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage Azure resources using SQL
custom_edit_url: null
image: /img/providers/azure/stackql-azure-provider-featured-image.png
---

import CopyableCode from '@site/src/components/CopyableCode/CopyableCode';




## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>tags_at_scope</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.resources.tags_at_scope" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | The ID of the tags wrapper resource. |
| <CopyableCode code="name" /> | `string` | The name of the tags wrapper resource. |
| <CopyableCode code="properties" /> | `object` | A dictionary of name and value pairs. |
| <CopyableCode code="type" /> | `string` | The type of the tags wrapper resource. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="scope" /> |  |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="scope, data__properties" /> | This operation allows adding or replacing the entire set of tags on the specified resource or subscription. The specified entity can have a maximum of 50 tags. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="scope" /> |  |
| <CopyableCode code="update" /> | `EXEC` | <CopyableCode code="scope" /> | This operation allows replacing, merging or selectively deleting tags on the specified resource or subscription. The specified entity can have a maximum of 50 tags at the end of the operation. The 'replace' option replaces the entire set of existing tags with a new set. The 'merge' option allows adding tags with new names and updating the values of tags with existing names. The 'delete' option allows selectively deleting tags based on given names or name/value pairs. |
