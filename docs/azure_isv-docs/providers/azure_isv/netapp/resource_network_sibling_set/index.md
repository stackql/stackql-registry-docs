---
title: resource_network_sibling_set
hide_title: false
hide_table_of_contents: false
keywords:
  - resource_network_sibling_set
  - netapp
  - azure_isv    
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
<tr><td><b>Name</b></td><td><code>resource_network_sibling_set</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure_isv.netapp.resource_network_sibling_set</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `networkFeatures` | `string` | Network features available to the volume, or current state of update. |
| `networkSiblingSetId` | `string` | Network Sibling Set ID for a group of volumes sharing networking resources in a subnet. |
| `networkSiblingSetStateId` | `string` | Network sibling set state Id identifying the current state of the sibling set. |
| `nicInfoList` | `array` | List of NIC information |
| `provisioningState` | `string` | Gets the status of the NetworkSiblingSet at the time the operation was called. |
| `subnetId` | `string` | The Azure Resource URI for a delegated subnet. Must have the delegation Microsoft.NetApp/volumes. Example /subscriptions/subscriptionId/resourceGroups/resourceGroup/providers/Microsoft.Network/virtualNetworks/testVnet/subnets/&#123;mySubnet&#125; |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `query_network_sibling_set` | `SELECT` | `location, subscriptionId, data__networkSiblingSetId, data__subnetId` | Get details of the specified network sibling set. |
| `update` | `EXEC` | `location, subscriptionId, data__networkFeatures, data__networkSiblingSetId, data__networkSiblingSetStateId, data__subnetId` | Update the network features of the specified network sibling set. |
