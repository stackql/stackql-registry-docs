---
title: sql_virtual_machines
hide_title: false
hide_table_of_contents: false
keywords:
  - sql_virtual_machines
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
<tr><td><b>Name</b></td><td><code>sql_virtual_machines</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.sql_vm.sql_virtual_machines</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `identity` | `object` | Azure Active Directory identity configuration for a resource. |
| `location` | `string` | Resource location. |
| `properties` | `object` | The SQL virtual machine properties. |
| `systemData` | `object` | Metadata pertaining to creation and last modification of the resource. |
| `tags` | `object` | Resource tags. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `resourceGroupName, sqlVirtualMachineName, subscriptionId` | Gets a SQL virtual machine. |
| `list` | `SELECT` | `subscriptionId` | Gets all SQL virtual machines in a subscription. |
| `list_by_resource_group` | `SELECT` | `resourceGroupName, subscriptionId` | Gets all SQL virtual machines in a resource group. |
| `list_by_sql_vm_group` | `SELECT` | `resourceGroupName, sqlVirtualMachineGroupName, subscriptionId` | Gets the list of sql virtual machines in a SQL virtual machine group. |
| `create_or_update` | `INSERT` | `resourceGroupName, sqlVirtualMachineName, subscriptionId, data__location` | Creates or updates a SQL virtual machine. |
| `delete` | `DELETE` | `resourceGroupName, sqlVirtualMachineName, subscriptionId` | Deletes a SQL virtual machine. |
| `_list` | `EXEC` | `subscriptionId` | Gets all SQL virtual machines in a subscription. |
| `_list_by_resource_group` | `EXEC` | `resourceGroupName, subscriptionId` | Gets all SQL virtual machines in a resource group. |
| `_list_by_sql_vm_group` | `EXEC` | `resourceGroupName, sqlVirtualMachineGroupName, subscriptionId` | Gets the list of sql virtual machines in a SQL virtual machine group. |
| `redeploy` | `EXEC` | `resourceGroupName, sqlVirtualMachineName, subscriptionId` | Uninstalls and reinstalls the SQL IaaS Extension. |
| `start_assessment` | `EXEC` | `resourceGroupName, sqlVirtualMachineName, subscriptionId` | Starts SQL best practices Assessment on SQL virtual machine. |
| `update` | `EXEC` | `resourceGroupName, sqlVirtualMachineName, subscriptionId` | Updates a SQL virtual machine. |
