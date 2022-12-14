---
title: virtual_machines
hide_title: false
hide_table_of_contents: false
keywords:
  - virtual_machines
  - system_center_vm_manager
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
<tr><td><b>Name</b></td><td><code>virtual_machines</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.system_center_vm_manager.virtual_machines</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | Resource Id |
| `name` | `string` | Resource Name |
| `extendedLocation` | `object` | The extended location. |
| `location` | `string` | Gets or sets the location. |
| `properties` | `object` | Defines the resource properties. |
| `systemData` | `object` | Metadata pertaining to creation and last modification of the resource. |
| `tags` | `object` | Resource tags |
| `type` | `string` | Resource Type |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `VirtualMachines_Get` | `SELECT` | `resourceGroupName, subscriptionId, virtualMachineName` | Implements VirtualMachine GET method. |
| `VirtualMachines_ListByResourceGroup` | `SELECT` | `resourceGroupName, subscriptionId` | List of VirtualMachines in a resource group. |
| `VirtualMachines_ListBySubscription` | `SELECT` | `subscriptionId` | List of VirtualMachines in a subscription. |
| `VirtualMachines_CreateOrUpdate` | `INSERT` | `resourceGroupName, subscriptionId, virtualMachineName, data__extendedLocation, data__location, data__properties` | Creates Or Updates virtual machines deployed on scvmm fabric. |
| `VirtualMachines_Delete` | `DELETE` | `resourceGroupName, subscriptionId, virtualMachineName` | Deletes a VirtualMachine deployed on ScVmm fabric. |
| `VirtualMachines_CreateCheckpoint` | `EXEC` | `resourceGroupName, subscriptionId, virtualMachineName` | Creates a checkpoint in virtual machine. |
| `VirtualMachines_DeleteCheckpoint` | `EXEC` | `resourceGroupName, subscriptionId, virtualMachineName` | Deletes a checkpoint in virtual machine. |
| `VirtualMachines_Restart` | `EXEC` | `resourceGroupName, subscriptionId, virtualMachineName` | Restart virtual machine. |
| `VirtualMachines_RestoreCheckpoint` | `EXEC` | `resourceGroupName, subscriptionId, virtualMachineName` | Restores to a checkpoint in virtual machine. |
| `VirtualMachines_Start` | `EXEC` | `resourceGroupName, subscriptionId, virtualMachineName` | Start virtual machine. |
| `VirtualMachines_Stop` | `EXEC` | `resourceGroupName, subscriptionId, virtualMachineName` | Stop virtual machine. |
| `VirtualMachines_Update` | `EXEC` | `resourceGroupName, subscriptionId, virtualMachineName` | Updates the VirtualMachines resource. |
