---
title: frontends_interface
hide_title: false
hide_table_of_contents: false
keywords:
  - frontends_interface
  - service_networking
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
<tr><td><b>Name</b></td><td><code>frontends_interface</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.service_networking.frontends_interface</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `location` | `string` | The geo-location where the resource lives |
| `properties` | `object` | Frontend Properties. |
| `tags` | `object` | Resource tags. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `frontendName, resourceGroupName, subscriptionId, trafficControllerName` | Get a Frontend |
| `list_by_traffic_controller` | `SELECT` | `resourceGroupName, subscriptionId, trafficControllerName` | List Frontend resources by TrafficController |
| `create_or_update` | `INSERT` | `frontendName, resourceGroupName, subscriptionId, trafficControllerName` | Create a Frontend |
| `delete` | `DELETE` | `frontendName, resourceGroupName, subscriptionId, trafficControllerName` | Delete a Frontend |
| `_list_by_traffic_controller` | `EXEC` | `resourceGroupName, subscriptionId, trafficControllerName` | List Frontend resources by TrafficController |
| `update` | `EXEC` | `frontendName, resourceGroupName, subscriptionId, trafficControllerName` | Update a Frontend |
