---
title: management_groups
hide_title: false
hide_table_of_contents: false
keywords:
  - management_groups
  - management_groups
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
<tr><td><b>Name</b></td><td><code>management_groups</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.management_groups.management_groups" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | The fully qualified ID for the management group.  For example, /providers/Microsoft.Management/managementGroups/0000000-0000-0000-0000-000000000000 |
| <CopyableCode code="name" /> | `string` | The name of the management group. For example, 00000000-0000-0000-0000-000000000000 |
| <CopyableCode code="properties" /> | `object` | The generic properties of a management group. |
| <CopyableCode code="type" /> | `string` | The type of the resource.  For example, Microsoft.Management/managementGroups |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="groupId" /> | Get the details of the management group.<br /> |
| <CopyableCode code="list" /> | `SELECT` |  | List management groups for the authenticated user.<br /> |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="groupId" /> | Create or update a management group.<br />If a management group is already created and a subsequent create request is issued with different properties, the management group properties will be updated.<br /> |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="groupId" /> | Delete management group.<br />If a management group contains child resources, the request will fail.<br /> |
| <CopyableCode code="update" /> | `EXEC` | <CopyableCode code="groupId" /> | Update a management group.<br /> |
