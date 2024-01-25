---
title: sites
hide_title: false
hide_table_of_contents: false
keywords:
  - sites
  - mobile_network
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
<tr><td><b>Name</b></td><td><code>sites</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.mobile_network.sites</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `location` | `string` | The geo-location where the resource lives |
| `properties` | `object` | Site properties. |
| `tags` | `object` | Resource tags. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `mobileNetworkName, resourceGroupName, siteName, subscriptionId` | Gets information about the specified mobile network site. |
| `list_by_mobile_network` | `SELECT` | `mobileNetworkName, resourceGroupName, subscriptionId` | Lists all sites in the mobile network. |
| `create_or_update` | `INSERT` | `mobileNetworkName, resourceGroupName, siteName, subscriptionId` | Creates or updates a mobile network site. Must be created in the same location as its parent mobile network. |
| `delete` | `DELETE` | `mobileNetworkName, resourceGroupName, siteName, subscriptionId` | Deletes the specified mobile network site. This will also delete any network functions that are a part of this site. |
| `_list_by_mobile_network` | `EXEC` | `mobileNetworkName, resourceGroupName, subscriptionId` | Lists all sites in the mobile network. |
