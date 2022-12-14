---
title: virtual_machine_scale_set_vm_extensions
hide_title: false
hide_table_of_contents: false
keywords:
  - virtual_machine_scale_set_vm_extensions
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
<tr><td><b>Name</b></td><td><code>virtual_machine_scale_set_vm_extensions</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.compute.virtual_machine_scale_set_vm_extensions</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | Resource Id |
| `name` | `string` | The name of the extension. |
| `properties` | `object` | Describes the properties of a Virtual Machine Extension. |
| `type` | `string` | Resource type |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `VirtualMachineScaleSetVMExtensions_Get` | `SELECT` | `instanceId, resourceGroupName, subscriptionId, vmExtensionName, vmScaleSetName` | The operation to get the VMSS VM extension. |
| `VirtualMachineScaleSetVMExtensions_List` | `SELECT` | `instanceId, resourceGroupName, subscriptionId, vmScaleSetName` | The operation to get all extensions of an instance in Virtual Machine Scaleset. |
| `VirtualMachineScaleSetVMExtensions_CreateOrUpdate` | `INSERT` | `instanceId, resourceGroupName, subscriptionId, vmExtensionName, vmScaleSetName` | The operation to create or update the VMSS VM extension. |
| `VirtualMachineScaleSetVMExtensions_Delete` | `DELETE` | `instanceId, resourceGroupName, subscriptionId, vmExtensionName, vmScaleSetName` | The operation to delete the VMSS VM extension. |
| `VirtualMachineScaleSetVMExtensions_Update` | `EXEC` | `instanceId, resourceGroupName, subscriptionId, vmExtensionName, vmScaleSetName` | The operation to update the VMSS VM extension. |
