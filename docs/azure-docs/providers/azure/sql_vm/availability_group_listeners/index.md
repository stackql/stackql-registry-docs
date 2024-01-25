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
  
    

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>availability_group_listeners</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.sql_vm.availability_group_listeners</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `properties` | `object` | The properties of an availability group listener. |
| `systemData` | `object` | Metadata pertaining to creation and last modification of the resource. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `availabilityGroupListenerName, resourceGroupName, sqlVirtualMachineGroupName, subscriptionId` | Gets an availability group listener. |
| `list_by_group` | `SELECT` | `resourceGroupName, sqlVirtualMachineGroupName, subscriptionId` | Lists all availability group listeners in a SQL virtual machine group. |
| `create_or_update` | `INSERT` | `availabilityGroupListenerName, resourceGroupName, sqlVirtualMachineGroupName, subscriptionId` | Creates or updates an availability group listener. |
| `delete` | `DELETE` | `availabilityGroupListenerName, resourceGroupName, sqlVirtualMachineGroupName, subscriptionId` | Deletes an availability group listener. |
| `_list_by_group` | `EXEC` | `resourceGroupName, sqlVirtualMachineGroupName, subscriptionId` | Lists all availability group listeners in a SQL virtual machine group. |
