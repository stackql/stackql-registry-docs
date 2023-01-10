---
title: virtual_machines
hide_title: false
hide_table_of_contents: false
keywords:
  - virtual_machines
  - connected_vsphere
  - azure_extras    
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
<tr><td><b>Id</b></td><td><code>azure_extras.connected_vsphere.virtual_machines</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | Gets or sets the Id. |
| `name` | `string` | Gets or sets the name. |
| `extendedLocation` | `object` | The extended location. |
| `kind` | `string` | Metadata used by portal/tooling/etc to render different UX experiences for resources of the same type; e.g. ApiApps are a kind of Microsoft.Web/sites type.  If supported, the resource provider must validate and persist this value. |
| `identity` | `object` | Identity for the resource. |
| `location` | `string` | Gets or sets the location. |
| `properties` | `object` | Defines the resource properties. |
| `tags` | `object` | Gets or sets the Resource tags. |
| `type` | `string` | Gets or sets the type of the resource. |
| `systemData` | `object` | Metadata pertaining to creation and last modification of the resource. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `VirtualMachines_Get` | `SELECT` | `api-version, resourceGroupName, subscriptionId, virtualMachineName` | Implements virtual machine GET method. |
| `VirtualMachines_List` | `SELECT` | `api-version, subscriptionId` | List of virtualMachines in a subscription. |
| `VirtualMachines_ListByResourceGroup` | `SELECT` | `api-version, resourceGroupName, subscriptionId` | List of virtualMachines in a resource group. |
| `VirtualMachines_Create` | `INSERT` | `api-version, resourceGroupName, subscriptionId, virtualMachineName, data__location, data__properties` | Create Or Update virtual machine. |
| `VirtualMachines_Delete` | `DELETE` | `api-version, resourceGroupName, subscriptionId, virtualMachineName` | Implements virtual machine DELETE method. |
| `VirtualMachines_AssessPatches` | `EXEC` | `name, resourceGroupName, subscriptionId` | The operation to assess patches on a vSphere VMware machine identity in Azure. |
| `VirtualMachines_InstallPatches` | `EXEC` | `name, resourceGroupName, subscriptionId, data__maximumDuration, data__rebootSetting` | The operation to install patches on a vSphere VMware machine identity in Azure. |
| `VirtualMachines_Restart` | `EXEC` | `api-version, resourceGroupName, subscriptionId, virtualMachineName` | Restart virtual machine. |
| `VirtualMachines_Start` | `EXEC` | `api-version, resourceGroupName, subscriptionId, virtualMachineName` | Start virtual machine. |
| `VirtualMachines_Stop` | `EXEC` | `api-version, resourceGroupName, subscriptionId, virtualMachineName` | Stop virtual machine. |
| `VirtualMachines_Update` | `EXEC` | `api-version, resourceGroupName, subscriptionId, virtualMachineName` | API to update certain properties of the virtual machine resource. |
