---
title: managed_network
hide_title: false
hide_table_of_contents: false
keywords:
  - managed_network
  - managed_network
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
<tr><td><b>Name</b></td><td><code>managed_network</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.managed_network.managed_network</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `tags` | `object` | Resource tags |
| `properties` | `object` | Properties of Managed Network |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `ManagedNetworks_Get` | `SELECT` | `managedNetworkName, resourceGroupName, subscriptionId` | The Get ManagedNetworks operation gets a Managed Network Resource, specified by the resource group and Managed Network name |
| `ManagedNetworks_ListByResourceGroup` | `SELECT` | `resourceGroupName, subscriptionId` | The ListByResourceGroup ManagedNetwork operation retrieves all the Managed Network resources in a resource group in a paginated format. |
| `ManagedNetworks_ListBySubscription` | `SELECT` | `subscriptionId` | The ListBySubscription  ManagedNetwork operation retrieves all the Managed Network Resources in the current subscription in a paginated format. |
| `ManagedNetworks_CreateOrUpdate` | `INSERT` | `managedNetworkName, resourceGroupName, subscriptionId` | The Put ManagedNetworks operation creates/updates a Managed Network Resource, specified by resource group and Managed Network name |
| `ManagedNetworks_Delete` | `DELETE` | `managedNetworkName, resourceGroupName, subscriptionId` | The Delete ManagedNetworks operation deletes a Managed Network Resource, specified by the  resource group and Managed Network name |
| `ManagedNetworks_Update` | `EXEC` | `managedNetworkName, resourceGroupName, subscriptionId` | Updates the specified Managed Network resource tags. |
