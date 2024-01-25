---
title: assignments_vm_ss
hide_title: false
hide_table_of_contents: false
keywords:
  - assignments_vm_ss
  - guest_configuration
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
<tr><td><b>Name</b></td><td><code>assignments_vm_ss</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.guest_configuration.assignments_vm_ss</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `properties` | `object` | Guest configuration assignment properties. |
| `systemData` | `object` | Metadata pertaining to creation and last modification of the resource. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `name, resourceGroupName, subscriptionId, vmssName` | Get information about a guest configuration assignment for VMSS |
| `list` | `SELECT` | `resourceGroupName, subscriptionId, vmssName` | List all guest configuration assignments for VMSS. |
| `create_or_update` | `INSERT` | `name, resourceGroupName, subscriptionId, vmssName` | Creates an association between a VMSS and guest configuration |
| `delete` | `DELETE` | `name, resourceGroupName, subscriptionId, vmssName` | Delete a guest configuration assignment for VMSS |
| `_list` | `EXEC` | `resourceGroupName, subscriptionId, vmssName` | List all guest configuration assignments for VMSS. |
