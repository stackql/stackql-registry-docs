---
title: assignments
hide_title: false
hide_table_of_contents: false
keywords:
  - assignments
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
<tr><td><b>Name</b></td><td><code>assignments</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.guest_configuration.assignments</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `systemData` | `object` | Metadata pertaining to creation and last modification of the resource. |
| `properties` | `object` | Guest configuration assignment properties. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `GuestConfigurationAssignments_Get` | `SELECT` | `guestConfigurationAssignmentName, resourceGroupName, subscriptionId, vmName` | Get information about a guest configuration assignment |
| `GuestConfigurationAssignments_List` | `SELECT` | `resourceGroupName, subscriptionId, vmName` | List all guest configuration assignments for a virtual machine. |
| `GuestConfigurationAssignments_CreateOrUpdate` | `INSERT` | `guestConfigurationAssignmentName, resourceGroupName, subscriptionId, vmName` | Creates an association between a VM and guest configuration |
| `GuestConfigurationAssignments_Delete` | `DELETE` | `guestConfigurationAssignmentName, resourceGroupName, subscriptionId, vmName` | Delete a guest configuration assignment |
| `GuestConfigurationAssignments_RGList` | `EXEC` | `resourceGroupName, subscriptionId` | List all guest configuration assignments for a resource group. |
| `GuestConfigurationAssignments_SubscriptionList` | `EXEC` | `subscriptionId` | List all guest configuration assignments for a subscription. |
