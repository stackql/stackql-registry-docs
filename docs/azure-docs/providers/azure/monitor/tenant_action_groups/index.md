---
title: tenant_action_groups
hide_title: false
hide_table_of_contents: false
keywords:
  - tenant_action_groups
  - monitor
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
<tr><td><b>Name</b></td><td><code>tenant_action_groups</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.monitor.tenant_action_groups" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | The resource Id. |
| <CopyableCode code="name" /> | `string` | The name of the resource. |
| <CopyableCode code="location" /> | `string` | The location of the resource. Azure Activity Log Alert rules are supported on Global, West Europe and North Europe regions. |
| <CopyableCode code="properties" /> | `object` | A tenant  action group. |
| <CopyableCode code="tags" /> | `object` | The tags of the resource. |
| <CopyableCode code="type" /> | `string` | The type of the resource. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="actionGroupName, managementGroupId, tenantId" /> | Get a tenant action group. |
| <CopyableCode code="list_by_management_group_id" /> | `SELECT` | <CopyableCode code="managementGroupId, tenantId" /> | Get a list of all tenant action groups in a management group. |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="actionGroupName, managementGroupId, tenantId" /> | Create a new tenant action group or update an existing one. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="actionGroupName, managementGroupId, tenantId" /> | Delete a tenant action group. |
| <CopyableCode code="update" /> | `EXEC` | <CopyableCode code="actionGroupName, managementGroupId, tenantId" /> | Updates an existing tenant action group's tags. To update other fields use the CreateOrUpdate method. |
