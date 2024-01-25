---
title: internet_gateway_rules
hide_title: false
hide_table_of_contents: false
keywords:
  - internet_gateway_rules
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
<tr><td><b>Name</b></td><td><code>internet_gateway_rules</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.managed_network_fabric.internet_gateway_rules</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `location` | `string` | The geo-location where the resource lives |
| `properties` | `object` | Internet Gateway Rule Properties defines the resource properties. |
| `tags` | `object` | Resource tags. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `internetGatewayRuleName, resourceGroupName, subscriptionId` | Gets an Internet Gateway Rule resource. |
| `list_by_resource_group` | `SELECT` | `resourceGroupName, subscriptionId` | Implements Internet Gateway Rules list by resource group GET method. |
| `list_by_subscription` | `SELECT` | `subscriptionId` | List all Internet Gateway rules in the given subscription. |
| `create` | `INSERT` | `internetGatewayRuleName, resourceGroupName, subscriptionId, data__properties` | Creates an Internet Gateway rule resource. |
| `delete` | `DELETE` | `internetGatewayRuleName, resourceGroupName, subscriptionId` | Implements Internet Gateway Rules DELETE method. |
| `_list_by_resource_group` | `EXEC` | `resourceGroupName, subscriptionId` | Implements Internet Gateway Rules list by resource group GET method. |
| `_list_by_subscription` | `EXEC` | `subscriptionId` | List all Internet Gateway rules in the given subscription. |
| `update` | `EXEC` | `internetGatewayRuleName, resourceGroupName, subscriptionId` | API to update certain properties of the Internet Gateway Rule resource. |
