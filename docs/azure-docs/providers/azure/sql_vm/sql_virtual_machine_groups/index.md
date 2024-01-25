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
  
    

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>sql_virtual_machine_groups</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.sql_vm.sql_virtual_machine_groups</code></td></tr>
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
| `get` | `SELECT` | `resourceGroupName, sqlVirtualMachineGroupName, subscriptionId` | Gets a SQL virtual machine group. |
| `list` | `SELECT` | `subscriptionId` | Gets all SQL virtual machine groups in a subscription. |
| `list_by_resource_group` | `SELECT` | `resourceGroupName, subscriptionId` | Gets all SQL virtual machine groups in a resource group. |
| `create_or_update` | `INSERT` | `resourceGroupName, sqlVirtualMachineGroupName, subscriptionId, data__location` | Creates or updates a SQL virtual machine group. |
| `delete` | `DELETE` | `resourceGroupName, sqlVirtualMachineGroupName, subscriptionId` | Deletes a SQL virtual machine group. |
| `_list` | `EXEC` | `subscriptionId` | Gets all SQL virtual machine groups in a subscription. |
| `_list_by_resource_group` | `EXEC` | `resourceGroupName, subscriptionId` | Gets all SQL virtual machine groups in a resource group. |
| `update` | `EXEC` | `resourceGroupName, sqlVirtualMachineGroupName, subscriptionId` | Updates SQL virtual machine group tags. |
