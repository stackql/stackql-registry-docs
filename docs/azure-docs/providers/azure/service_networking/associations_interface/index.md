---
title: associations_interface
hide_title: false
hide_table_of_contents: false
keywords:
  - associations_interface
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
<tr><td><b>Name</b></td><td><code>associations_interface</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.service_networking.associations_interface</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `location` | `string` | The geo-location where the resource lives |
| `properties` | `object` | Association Properties. |
| `tags` | `object` | Resource tags. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `associationName, resourceGroupName, subscriptionId, trafficControllerName` | Get a Association |
| `list_by_traffic_controller` | `SELECT` | `resourceGroupName, subscriptionId, trafficControllerName` | List Association resources by TrafficController |
| `create_or_update` | `INSERT` | `associationName, resourceGroupName, subscriptionId, trafficControllerName` | Create a Association |
| `delete` | `DELETE` | `associationName, resourceGroupName, subscriptionId, trafficControllerName` | Delete a Association |
| `_list_by_traffic_controller` | `EXEC` | `resourceGroupName, subscriptionId, trafficControllerName` | List Association resources by TrafficController |
| `update` | `EXEC` | `associationName, resourceGroupName, subscriptionId, trafficControllerName` | Update a Association |
