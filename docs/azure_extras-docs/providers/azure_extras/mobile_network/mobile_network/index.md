---
title: mobile_network
hide_title: false
hide_table_of_contents: false
keywords:
  - mobile_network
  - mobile_network
  - azure_extras    
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
<tr><td><b>Name</b></td><td><code>mobile_network</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure_extras.mobile_network.mobile_network</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `systemData` | `object` | Metadata pertaining to creation and last modification of the resource. |
| `tags` | `object` | Resource tags. |
| `location` | `string` | The geo-location where the resource lives |
| `properties` | `object` | Mobile network properties. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `MobileNetworks_Get` | `SELECT` | `mobileNetworkName, resourceGroupName, subscriptionId` | Gets information about the specified mobile network. |
| `MobileNetworks_ListByResourceGroup` | `SELECT` | `resourceGroupName, subscriptionId` | Lists all the mobile networks in a resource group. |
| `MobileNetworks_ListBySubscription` | `SELECT` | `subscriptionId` | Lists all the mobile networks in a subscription. |
| `MobileNetworks_CreateOrUpdate` | `INSERT` | `mobileNetworkName, resourceGroupName, subscriptionId, data__properties` | Creates or updates a mobile network. |
| `MobileNetworks_Delete` | `DELETE` | `mobileNetworkName, resourceGroupName, subscriptionId` | Deletes the specified mobile network. |
| `MobileNetworks_ListSimIds` | `EXEC` | `mobileNetworkName, resourceGroupName, subscriptionId` | Lists the IDs of all provisioned SIMs in a mobile network |
| `MobileNetworks_UpdateTags` | `EXEC` | `mobileNetworkName, resourceGroupName, subscriptionId` | Updates mobile network tags. |
