---
title: internet_gateways
hide_title: false
hide_table_of_contents: false
keywords:
  - internet_gateways
  - managed_network_fabric
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
<tr><td><b>Name</b></td><td><code>internet_gateways</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.managed_network_fabric.internet_gateways</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `location` | `string` | The geo-location where the resource lives |
| `properties` | `object` | Internet Gateway Properties defines the properties of the resource. |
| `tags` | `object` | Resource tags. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `internetGatewayName, resourceGroupName, subscriptionId` | Implements Gateway GET method. |
| `list_by_resource_group` | `SELECT` | `resourceGroupName, subscriptionId` | Displays Internet Gateways list by resource group GET method. |
| `list_by_subscription` | `SELECT` | `subscriptionId` | Displays Internet Gateways list by subscription GET method. |
| `create` | `INSERT` | `internetGatewayName, resourceGroupName, subscriptionId, data__properties` | Creates a Network Fabric Service Internet Gateway resource instance. |
| `delete` | `DELETE` | `internetGatewayName, resourceGroupName, subscriptionId` | Execute a delete on Network Fabric Service Internet Gateway. |
| `_list_by_resource_group` | `EXEC` | `resourceGroupName, subscriptionId` | Displays Internet Gateways list by resource group GET method. |
| `_list_by_subscription` | `EXEC` | `subscriptionId` | Displays Internet Gateways list by subscription GET method. |
| `update` | `EXEC` | `internetGatewayName, resourceGroupName, subscriptionId` | Execute patch on Network Fabric Service Internet Gateway. |
