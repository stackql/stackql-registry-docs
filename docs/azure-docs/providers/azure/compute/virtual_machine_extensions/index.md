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
| `location` | `string` | Resource location |
| `properties` | `object` | Describes the properties of a Virtual Machine Extension. |
| `tags` | `object` | Resource tags |
| `type` | `string` | Resource type |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `resourceGroupName, subscriptionId, vmExtensionName, vmName` | The operation to get the extension. |
| `list` | `SELECT` | `resourceGroupName, subscriptionId, vmName` | The operation to get all extensions of a Virtual Machine. |
| `create_or_update` | `INSERT` | `resourceGroupName, subscriptionId, vmExtensionName, vmName` | The operation to create or update the extension. |
| `delete` | `DELETE` | `resourceGroupName, subscriptionId, vmExtensionName, vmName` | The operation to delete the extension. |
| `_list` | `EXEC` | `resourceGroupName, subscriptionId, vmName` | The operation to get all extensions of a Virtual Machine. |
| `update` | `EXEC` | `resourceGroupName, subscriptionId, vmExtensionName, vmName` | The operation to update the extension. |
