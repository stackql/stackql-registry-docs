---
title: sql_virtual_machine_groups
hide_title: false
hide_table_of_contents: false
keywords:
  - sql_virtual_machine_groups
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
<tr><td><b>Name</b></td><td><code>sql_virtual_machine_groups</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.sql_vm.sql_virtual_machine_groups" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="location" /> | `string` | Resource location. |
| <CopyableCode code="properties" /> | `object` | The properties of a SQL virtual machine group. |
| <CopyableCode code="systemData" /> | `object` | Metadata pertaining to creation and last modification of the resource. |
| <CopyableCode code="tags" /> | `object` | Resource tags. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="resourceGroupName, sqlVirtualMachineGroupName, subscriptionId" /> | Gets a SQL virtual machine group. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="subscriptionId" /> | Gets all SQL virtual machine groups in a subscription. |
| <CopyableCode code="list_by_resource_group" /> | `SELECT` | <CopyableCode code="resourceGroupName, subscriptionId" /> | Gets all SQL virtual machine groups in a resource group. |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="resourceGroupName, sqlVirtualMachineGroupName, subscriptionId, data__location" /> | Creates or updates a SQL virtual machine group. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="resourceGroupName, sqlVirtualMachineGroupName, subscriptionId" /> | Deletes a SQL virtual machine group. |
| <CopyableCode code="_list" /> | `EXEC` | <CopyableCode code="subscriptionId" /> | Gets all SQL virtual machine groups in a subscription. |
| <CopyableCode code="_list_by_resource_group" /> | `EXEC` | <CopyableCode code="resourceGroupName, subscriptionId" /> | Gets all SQL virtual machine groups in a resource group. |
| <CopyableCode code="update" /> | `EXEC` | <CopyableCode code="resourceGroupName, sqlVirtualMachineGroupName, subscriptionId" /> | Updates SQL virtual machine group tags. |
