---
title: routing_intent
hide_title: false
hide_table_of_contents: false
keywords:
  - routing_intent
  - network
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
<tr><td><b>Name</b></td><td><code>routing_intent</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.network.routing_intent</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | Resource ID. |
| `name` | `string` | The name of the resource that is unique within a resource group. This name can be used to access the resource. |
| `properties` | `object` | The properties of a RoutingIntent resource. |
| `type` | `string` | Resource type. |
| `etag` | `string` | A unique read-only string that changes whenever the resource is updated. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `RoutingIntent_Get` | `SELECT` | `resourceGroupName, routingIntentName, subscriptionId, virtualHubName` | Retrieves the details of a RoutingIntent. |
| `RoutingIntent_List` | `SELECT` | `resourceGroupName, subscriptionId, virtualHubName` | Retrieves the details of all RoutingIntent child resources of the VirtualHub. |
| `RoutingIntent_CreateOrUpdate` | `INSERT` | `resourceGroupName, routingIntentName, subscriptionId, virtualHubName` | Creates a RoutingIntent resource if it doesn't exist else updates the existing RoutingIntent. |
| `RoutingIntent_Delete` | `DELETE` | `resourceGroupName, routingIntentName, subscriptionId, virtualHubName` | Deletes a RoutingIntent. |
