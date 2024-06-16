---
title: availability_group_listeners
hide_title: false
hide_table_of_contents: false
keywords:
  - availability_group_listeners
  - sql_vm
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
<tr><td><b>Name</b></td><td><code>availability_group_listeners</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.sql_vm.availability_group_listeners" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="properties" /> | `object` | The properties of an availability group listener. |
| <CopyableCode code="systemData" /> | `object` | Metadata pertaining to creation and last modification of the resource. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="availabilityGroupListenerName, resourceGroupName, sqlVirtualMachineGroupName, subscriptionId" /> | Gets an availability group listener. |
| <CopyableCode code="list_by_group" /> | `SELECT` | <CopyableCode code="resourceGroupName, sqlVirtualMachineGroupName, subscriptionId" /> | Lists all availability group listeners in a SQL virtual machine group. |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="availabilityGroupListenerName, resourceGroupName, sqlVirtualMachineGroupName, subscriptionId" /> | Creates or updates an availability group listener. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="availabilityGroupListenerName, resourceGroupName, sqlVirtualMachineGroupName, subscriptionId" /> | Deletes an availability group listener. |
