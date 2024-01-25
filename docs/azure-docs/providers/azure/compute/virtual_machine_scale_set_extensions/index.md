---
title: virtual_machine_scale_set_extensions
hide_title: false
hide_table_of_contents: false
keywords:
  - virtual_machine_scale_set_extensions
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
<tr><td><b>Name</b></td><td><code>virtual_machine_scale_set_extensions</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.compute.virtual_machine_scale_set_extensions</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | Resource Id |
| `name` | `string` | The name of the extension. |
| `properties` | `object` | Describes the properties of a Virtual Machine Scale Set Extension. |
| `type` | `string` | Resource type |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `resourceGroupName, subscriptionId, vmScaleSetName, vmssExtensionName` | The operation to get the extension. |
| `list` | `SELECT` | `resourceGroupName, subscriptionId, vmScaleSetName` | Gets a list of all extensions in a VM scale set. |
| `create_or_update` | `INSERT` | `resourceGroupName, subscriptionId, vmScaleSetName, vmssExtensionName` | The operation to create or update an extension. |
| `delete` | `DELETE` | `resourceGroupName, subscriptionId, vmScaleSetName, vmssExtensionName` | The operation to delete the extension. |
| `_list` | `EXEC` | `resourceGroupName, subscriptionId, vmScaleSetName` | Gets a list of all extensions in a VM scale set. |
| `update` | `EXEC` | `resourceGroupName, subscriptionId, vmScaleSetName, vmssExtensionName` | The operation to update an extension. |
