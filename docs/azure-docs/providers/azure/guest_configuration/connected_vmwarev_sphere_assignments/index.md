---
title: connected_vmwarev_sphere_assignments
hide_title: false
hide_table_of_contents: false
keywords:
  - connected_vmwarev_sphere_assignments
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
<tr><td><b>Name</b></td><td><code>connected_vmwarev_sphere_assignments</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.guest_configuration.connected_vmwarev_sphere_assignments</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `properties` | `object` | Guest configuration assignment properties. |
| `systemData` | `object` | Metadata pertaining to creation and last modification of the resource. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `guestConfigurationAssignmentName, resourceGroupName, subscriptionId, vmName` | Get information about a guest configuration assignment |
| `list` | `SELECT` | `resourceGroupName, subscriptionId, vmName` | List all guest configuration assignments for an ARC machine. |
| `create_or_update` | `INSERT` | `guestConfigurationAssignmentName, resourceGroupName, subscriptionId, vmName` | Creates an association between a Connected VM Sphere machine and guest configuration |
| `delete` | `DELETE` | `guestConfigurationAssignmentName, resourceGroupName, subscriptionId, vmName` | Delete a guest configuration assignment |
| `_list` | `EXEC` | `resourceGroupName, subscriptionId, vmName` | List all guest configuration assignments for an ARC machine. |
