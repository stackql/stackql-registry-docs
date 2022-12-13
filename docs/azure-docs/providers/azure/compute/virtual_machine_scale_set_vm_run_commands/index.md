---
title: virtual_machine_scale_set_vm_run_commands
hide_title: false
hide_table_of_contents: false
keywords:
  - virtual_machine_scale_set_vm_run_commands
  - compute
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
<tr><td><b>Name</b></td><td><code>virtual_machine_scale_set_vm_run_commands</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.compute.virtual_machine_scale_set_vm_run_commands</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | Resource Id |
| `name` | `string` | Resource name |
| `tags` | `object` | Resource tags |
| `type` | `string` | Resource type |
| `location` | `string` | Resource location |
| `properties` | `object` | Describes the properties of a Virtual Machine run command. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `VirtualMachineScaleSetVMRunCommands_Get` | `SELECT` | `instanceId, resourceGroupName, runCommandName, subscriptionId, vmScaleSetName` | The operation to get the VMSS VM run command. |
| `VirtualMachineScaleSetVMRunCommands_List` | `SELECT` | `instanceId, resourceGroupName, subscriptionId, vmScaleSetName` | The operation to get all run commands of an instance in Virtual Machine Scaleset. |
| `VirtualMachineScaleSetVMRunCommands_CreateOrUpdate` | `INSERT` | `instanceId, resourceGroupName, runCommandName, subscriptionId, vmScaleSetName` | The operation to create or update the VMSS VM run command. |
| `VirtualMachineScaleSetVMRunCommands_Delete` | `DELETE` | `instanceId, resourceGroupName, runCommandName, subscriptionId, vmScaleSetName` | The operation to delete the VMSS VM run command. |
| `VirtualMachineScaleSetVMRunCommands_Update` | `EXEC` | `instanceId, resourceGroupName, runCommandName, subscriptionId, vmScaleSetName` | The operation to update the VMSS VM run command. |
