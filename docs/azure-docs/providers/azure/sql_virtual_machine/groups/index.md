---
title: groups
hide_title: false
hide_table_of_contents: false
keywords:
  - groups
  - sql_virtual_machine
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
<tr><td><b>Name</b></td><td><code>groups</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.sql_virtual_machine.groups</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `location` | `string` | Resource location. |
| `properties` | `object` | The properties of a SQL virtual machine group. |
| `systemData` | `object` | Metadata pertaining to creation and last modification of the resource. |
| `tags` | `object` | Resource tags. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `SqlVirtualMachineGroups_Get` | `SELECT` | `resourceGroupName, sqlVirtualMachineGroupName, subscriptionId` | Gets a SQL virtual machine group. |
| `SqlVirtualMachineGroups_List` | `SELECT` | `subscriptionId` | Gets all SQL virtual machine groups in a subscription. |
| `SqlVirtualMachineGroups_ListByResourceGroup` | `SELECT` | `resourceGroupName, subscriptionId` | Gets all SQL virtual machine groups in a resource group. |
| `SqlVirtualMachineGroups_CreateOrUpdate` | `INSERT` | `resourceGroupName, sqlVirtualMachineGroupName, subscriptionId, data__location` | Creates or updates a SQL virtual machine group. |
| `SqlVirtualMachineGroups_Delete` | `DELETE` | `resourceGroupName, sqlVirtualMachineGroupName, subscriptionId` | Deletes a SQL virtual machine group. |
| `SqlVirtualMachineGroups_Update` | `EXEC` | `resourceGroupName, sqlVirtualMachineGroupName, subscriptionId` | Updates SQL virtual machine group tags. |
