---
title: hcrp_assignments
hide_title: false
hide_table_of_contents: false
keywords:
  - hcrp_assignments
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
<tr><td><b>Name</b></td><td><code>hcrp_assignments</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.guest_configuration.hcrp_assignments</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `properties` | `object` | Guest configuration assignment properties. |
| `systemData` | `object` | Metadata pertaining to creation and last modification of the resource. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `guestConfigurationAssignmentName, machineName, resourceGroupName, subscriptionId` | Get information about a guest configuration assignment |
| `list` | `SELECT` | `machineName, resourceGroupName, subscriptionId` | List all guest configuration assignments for an ARC machine. |
| `create_or_update` | `INSERT` | `guestConfigurationAssignmentName, machineName, resourceGroupName, subscriptionId` | Creates an association between a ARC machine and guest configuration |
| `delete` | `DELETE` | `guestConfigurationAssignmentName, machineName, resourceGroupName, subscriptionId` | Delete a guest configuration assignment |
| `_list` | `EXEC` | `machineName, resourceGroupName, subscriptionId` | List all guest configuration assignments for an ARC machine. |
