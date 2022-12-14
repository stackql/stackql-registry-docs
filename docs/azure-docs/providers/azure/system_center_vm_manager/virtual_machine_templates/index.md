---
title: virtual_machine_templates
hide_title: false
hide_table_of_contents: false
keywords:
  - virtual_machine_templates
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
<tr><td><b>Name</b></td><td><code>virtual_machine_templates</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.system_center_vm_manager.virtual_machine_templates</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | Resource Id |
| `name` | `string` | Resource Name |
| `properties` | `object` | Defines the resource properties. |
| `systemData` | `object` | Metadata pertaining to creation and last modification of the resource. |
| `tags` | `object` | Resource tags |
| `type` | `string` | Resource Type |
| `extendedLocation` | `object` | The extended location. |
| `location` | `string` | Gets or sets the location. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `VirtualMachineTemplates_Get` | `SELECT` | `resourceGroupName, subscriptionId, virtualMachineTemplateName` | Implements VirtualMachineTemplate GET method. |
| `VirtualMachineTemplates_ListByResourceGroup` | `SELECT` | `resourceGroupName, subscriptionId` | List of VirtualMachineTemplates in a resource group. |
| `VirtualMachineTemplates_ListBySubscription` | `SELECT` | `subscriptionId` | List of VirtualMachineTemplates in a subscription. |
| `VirtualMachineTemplates_CreateOrUpdate` | `INSERT` | `resourceGroupName, subscriptionId, virtualMachineTemplateName, data__extendedLocation, data__location, data__properties` | Onboards the ScVmm VM Template as an Azure VM Template resource. |
| `VirtualMachineTemplates_Delete` | `DELETE` | `resourceGroupName, subscriptionId, virtualMachineTemplateName` | Deregisters the ScVmm VM Template from Azure. |
| `VirtualMachineTemplates_Update` | `EXEC` | `resourceGroupName, subscriptionId, virtualMachineTemplateName` | Updates the VirtualMachineTemplate resource. |
