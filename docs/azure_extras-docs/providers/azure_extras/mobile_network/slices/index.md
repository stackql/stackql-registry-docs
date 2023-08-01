---
title: slices
hide_title: false
hide_table_of_contents: false
keywords:
  - slices
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
<tr><td><b>Name</b></td><td><code>slices</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure_extras.mobile_network.slices</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `systemData` | `object` | Metadata pertaining to creation and last modification of the resource. |
| `tags` | `object` | Resource tags. |
| `location` | `string` | The geo-location where the resource lives |
| `properties` | `object` | Network slice properties. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `Slices_Get` | `SELECT` | `mobileNetworkName, resourceGroupName, sliceName, subscriptionId` | Gets information about the specified network slice. |
| `Slices_ListByMobileNetwork` | `SELECT` | `mobileNetworkName, resourceGroupName, subscriptionId` | Lists all slices in the mobile network. |
| `Slices_CreateOrUpdate` | `INSERT` | `mobileNetworkName, resourceGroupName, sliceName, subscriptionId, data__properties` | Creates or updates a network slice. |
| `Slices_Delete` | `DELETE` | `mobileNetworkName, resourceGroupName, sliceName, subscriptionId` | Deletes the specified network slice. |
| `Slices_UpdateTags` | `EXEC` | `mobileNetworkName, resourceGroupName, sliceName, subscriptionId` | Updates slice tags. |
