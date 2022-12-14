---
title: peering_policies
hide_title: false
hide_table_of_contents: false
keywords:
  - peering_policies
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
<tr><td><b>Name</b></td><td><code>peering_policies</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.managed_network.peering_policies</code></td></tr>
</tbody></table>

## Fields
`SELECT` not supported for this resource, use `SHOW METHODS` to view available operations for the resource and then invoke a supported method using the `EXEC` command  
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `ManagedNetworkPeeringPolicies_Get` | `SELECT` | `managedNetworkName, managedNetworkPeeringPolicyName, resourceGroupName, subscriptionId` | The Get ManagedNetworkPeeringPolicies operation gets a Managed Network Peering Policy resource, specified by the  resource group, Managed Network name, and peering policy name |
| `ManagedNetworkPeeringPolicies_ListByManagedNetwork` | `SELECT` | `managedNetworkName, resourceGroupName, subscriptionId` | The ListByManagedNetwork PeeringPolicies operation retrieves all the Managed Network Peering Policies in a specified Managed Network, in a paginated format. |
| `ManagedNetworkPeeringPolicies_CreateOrUpdate` | `INSERT` | `managedNetworkName, managedNetworkPeeringPolicyName, resourceGroupName, subscriptionId` | The Put ManagedNetworkPeeringPolicies operation creates/updates a new Managed Network Peering Policy |
| `ManagedNetworkPeeringPolicies_Delete` | `DELETE` | `managedNetworkName, managedNetworkPeeringPolicyName, resourceGroupName, subscriptionId` | The Delete ManagedNetworkPeeringPolicies operation deletes a Managed Network Peering Policy, specified by the  resource group, Managed Network name, and peering policy name |
