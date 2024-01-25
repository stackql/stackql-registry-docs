---
title: route_policies
hide_title: false
hide_table_of_contents: false
keywords:
  - route_policies
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
<tr><td><b>Name</b></td><td><code>route_policies</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.managed_network_fabric.route_policies</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `location` | `string` | The geo-location where the resource lives |
| `properties` | `object` | RoutePolicyProperties defines the resource properties. |
| `tags` | `object` | Resource tags. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `resourceGroupName, routePolicyName, subscriptionId` | Implements Route Policy GET method. |
| `list_by_resource_group` | `SELECT` | `resourceGroupName, subscriptionId` | Implements RoutePolicies list by resource group GET method. |
| `list_by_subscription` | `SELECT` | `subscriptionId` | Implements RoutePolicies list by subscription GET method. |
| `create` | `INSERT` | `resourceGroupName, routePolicyName, subscriptionId, data__location, data__properties` | Implements Route Policy PUT method. |
| `delete` | `DELETE` | `resourceGroupName, routePolicyName, subscriptionId` | Implements Route Policy DELETE method. |
| `_list_by_resource_group` | `EXEC` | `resourceGroupName, subscriptionId` | Implements RoutePolicies list by resource group GET method. |
| `_list_by_subscription` | `EXEC` | `subscriptionId` | Implements RoutePolicies list by subscription GET method. |
| `commit_configuration` | `EXEC` | `resourceGroupName, routePolicyName, subscriptionId` | Commits the configuration of the given resources. |
| `update` | `EXEC` | `resourceGroupName, routePolicyName, subscriptionId` | API to update certain properties of the Route Policy resource. |
| `validate_configuration` | `EXEC` | `resourceGroupName, routePolicyName, subscriptionId` | Validates the configuration of the resources. |
