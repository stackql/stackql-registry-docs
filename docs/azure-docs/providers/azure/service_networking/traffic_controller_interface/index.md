---
title: traffic_controller_interface
hide_title: false
hide_table_of_contents: false
keywords:
  - traffic_controller_interface
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
<tr><td><b>Name</b></td><td><code>traffic_controller_interface</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.service_networking.traffic_controller_interface</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `location` | `string` | The geo-location where the resource lives |
| `properties` | `object` | Traffic Controller Properties. |
| `tags` | `object` | Resource tags. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `resourceGroupName, subscriptionId, trafficControllerName` | Get a TrafficController |
| `list_by_resource_group` | `SELECT` | `resourceGroupName, subscriptionId` | List TrafficController resources by resource group |
| `list_by_subscription` | `SELECT` | `subscriptionId` | List TrafficController resources by subscription ID |
| `create_or_update` | `INSERT` | `resourceGroupName, subscriptionId, trafficControllerName` | Create a TrafficController |
| `delete` | `DELETE` | `resourceGroupName, subscriptionId, trafficControllerName` | Delete a TrafficController |
| `_list_by_resource_group` | `EXEC` | `resourceGroupName, subscriptionId` | List TrafficController resources by resource group |
| `_list_by_subscription` | `EXEC` | `subscriptionId` | List TrafficController resources by subscription ID |
| `update` | `EXEC` | `resourceGroupName, subscriptionId, trafficControllerName` | Update a TrafficController |
