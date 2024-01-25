---
title: services
hide_title: false
hide_table_of_contents: false
keywords:
  - services
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
<tr><td><b>Name</b></td><td><code>services</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.mobile_network.services</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `location` | `string` | The geo-location where the resource lives |
| `properties` | `object` | Service properties. |
| `tags` | `object` | Resource tags. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `mobileNetworkName, resourceGroupName, serviceName, subscriptionId` | Gets information about the specified service. |
| `list_by_mobile_network` | `SELECT` | `mobileNetworkName, resourceGroupName, subscriptionId` | Gets all the services in a mobile network. |
| `create_or_update` | `INSERT` | `mobileNetworkName, resourceGroupName, serviceName, subscriptionId, data__properties` | Creates or updates a service. Must be created in the same location as its parent mobile network. |
| `delete` | `DELETE` | `mobileNetworkName, resourceGroupName, serviceName, subscriptionId` | Deletes the specified service. |
| `_list_by_mobile_network` | `EXEC` | `mobileNetworkName, resourceGroupName, subscriptionId` | Gets all the services in a mobile network. |
