---
title: virtual_machine_extensions
hide_title: false
hide_table_of_contents: false
keywords:
  - virtual_machine_extensions
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
<tr><td><b>Name</b></td><td><code>virtual_machine_extensions</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.compute.virtual_machine_extensions</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | Resource Id |
| `name` | `string` | Resource name |
| `type` | `string` | Resource type |
| `location` | `string` | Resource location |
| `properties` | `object` | Describes the properties of a Virtual Machine Extension. |
| `tags` | `object` | Resource tags |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `VirtualMachineExtensions_Get` | `SELECT` | `resourceGroupName, subscriptionId, vmExtensionName, vmName` | The operation to get the extension. |
| `VirtualMachineExtensions_List` | `SELECT` | `resourceGroupName, subscriptionId, vmName` | The operation to get all extensions of a Virtual Machine. |
| `VirtualMachineExtensions_CreateOrUpdate` | `INSERT` | `resourceGroupName, subscriptionId, vmExtensionName, vmName` | The operation to create or update the extension. |
| `VirtualMachineExtensions_Delete` | `DELETE` | `resourceGroupName, subscriptionId, vmExtensionName, vmName` | The operation to delete the extension. |
| `VirtualMachineExtensions_Update` | `EXEC` | `resourceGroupName, subscriptionId, vmExtensionName, vmName` | The operation to update the extension. |
