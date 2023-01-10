---
title: data_networks
hide_title: false
hide_table_of_contents: false
keywords:
  - data_networks
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
<tr><td><b>Name</b></td><td><code>data_networks</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure_extras.mobile_network.data_networks</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `properties` | `object` | Data network properties. |
| `systemData` | `object` | Metadata pertaining to creation and last modification of the resource. |
| `tags` | `object` | Resource tags. |
| `location` | `string` | The geo-location where the resource lives |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `DataNetworks_Get` | `SELECT` | `dataNetworkName, mobileNetworkName, resourceGroupName, subscriptionId` | Gets information about the specified data network. |
| `DataNetworks_ListByMobileNetwork` | `SELECT` | `mobileNetworkName, resourceGroupName, subscriptionId` | Lists all data networks in the mobile network. |
| `DataNetworks_CreateOrUpdate` | `INSERT` | `dataNetworkName, mobileNetworkName, resourceGroupName, subscriptionId` | Creates or updates a data network. |
| `DataNetworks_Delete` | `DELETE` | `dataNetworkName, mobileNetworkName, resourceGroupName, subscriptionId` | Deletes the specified data network. |
| `DataNetworks_UpdateTags` | `EXEC` | `dataNetworkName, mobileNetworkName, resourceGroupName, subscriptionId` | Updates data network tags. |
