---
title: virtual_machines
hide_title: false
hide_table_of_contents: false
keywords:
  - virtual_machines
  - nexus
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
<tr><td><b>Name</b></td><td><code>virtual_machines</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.nexus.virtual_machines</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `extendedLocation` | `object` |  |
| `location` | `string` | The geo-location where the resource lives |
| `properties` | `object` |  |
| `tags` | `object` | Resource tags. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `resourceGroupName, subscriptionId, virtualMachineName` | Get properties of the provided virtual machine. |
| `list_by_resource_group` | `SELECT` | `resourceGroupName, subscriptionId` | Get a list of virtual machines in the provided resource group. |
| `list_by_subscription` | `SELECT` | `subscriptionId` | Get a list of virtual machines in the provided subscription. |
| `create_or_update` | `INSERT` | `resourceGroupName, subscriptionId, virtualMachineName, data__extendedLocation, data__properties` | Create a new virtual machine or update the properties of the existing virtual machine. |
| `delete` | `DELETE` | `resourceGroupName, subscriptionId, virtualMachineName` | Delete the provided virtual machine. |
| `_list_by_resource_group` | `EXEC` | `resourceGroupName, subscriptionId` | Get a list of virtual machines in the provided resource group. |
| `_list_by_subscription` | `EXEC` | `subscriptionId` | Get a list of virtual machines in the provided subscription. |
| `power_off` | `EXEC` | `resourceGroupName, subscriptionId, virtualMachineName` | Power off the provided virtual machine. |
| `reimage` | `EXEC` | `resourceGroupName, subscriptionId, virtualMachineName` | Reimage the provided virtual machine. |
| `restart` | `EXEC` | `resourceGroupName, subscriptionId, virtualMachineName` | Restart the provided virtual machine. |
| `start` | `EXEC` | `resourceGroupName, subscriptionId, virtualMachineName` | Start the provided virtual machine. |
| `update` | `EXEC` | `resourceGroupName, subscriptionId, virtualMachineName` | Patch the properties of the provided virtual machine, or update the tags associated with the virtual machine. Properties and tag updates can be done independently. |
