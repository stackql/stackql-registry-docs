---
title: sql_virtual_machine
hide_title: false
hide_table_of_contents: false
keywords:
  - sql_virtual_machine
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
<tr><td><b>Name</b></td><td><code>sql_virtual_machine</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.sql_virtual_machine.sql_virtual_machine</code></td></tr>
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
| `SqlVirtualMachines_Get` | `SELECT` | `resourceGroupName, sqlVirtualMachineName, subscriptionId` | Gets a SQL virtual machine. |
| `SqlVirtualMachines_List` | `SELECT` | `subscriptionId` | Gets all SQL virtual machines in a subscription. |
| `SqlVirtualMachines_ListByResourceGroup` | `SELECT` | `resourceGroupName, subscriptionId` | Gets all SQL virtual machines in a resource group. |
| `SqlVirtualMachines_ListBySqlVmGroup` | `SELECT` | `resourceGroupName, sqlVirtualMachineGroupName, subscriptionId` | Gets the list of sql virtual machines in a SQL virtual machine group. |
| `SqlVirtualMachines_CreateOrUpdate` | `INSERT` | `resourceGroupName, sqlVirtualMachineName, subscriptionId, data__location` | Creates or updates a SQL virtual machine. |
| `SqlVirtualMachines_Delete` | `DELETE` | `resourceGroupName, sqlVirtualMachineName, subscriptionId` | Deletes a SQL virtual machine. |
| `SqlVirtualMachines_Redeploy` | `EXEC` | `resourceGroupName, sqlVirtualMachineName, subscriptionId` | Uninstalls and reinstalls the SQL Iaas Extension. |
| `SqlVirtualMachines_StartAssessment` | `EXEC` | `resourceGroupName, sqlVirtualMachineName, subscriptionId` | Starts Assessment on SQL virtual machine. |
| `SqlVirtualMachines_Update` | `EXEC` | `resourceGroupName, sqlVirtualMachineName, subscriptionId` | Updates a SQL virtual machine. |
