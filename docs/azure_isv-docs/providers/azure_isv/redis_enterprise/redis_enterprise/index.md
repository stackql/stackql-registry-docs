---
title: redis_enterprise
hide_title: false
hide_table_of_contents: false
keywords:
  - redis_enterprise
  - redis_enterprise
  - azure_isv    
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
<tr><td><b>Name</b></td><td><code>redis_enterprise</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure_isv.redis_enterprise.redis_enterprise</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `identity` | `object` | Managed service identity (system assigned and/or user assigned identities) |
| `location` | `string` | The geo-location where the resource lives |
| `properties` | `object` | Properties of RedisEnterprise clusters, as opposed to general resource properties like location, tags |
| `sku` | `object` | SKU parameters supplied to the create RedisEnterprise operation. |
| `tags` | `object` | Resource tags. |
| `zones` | `array` | The Availability Zones where this cluster will be deployed. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `clusterName, resourceGroupName, subscriptionId` | Gets information about a RedisEnterprise cluster |
| `list` | `SELECT` | `subscriptionId` | Gets all RedisEnterprise clusters in the specified subscription. |
| `list_by_resource_group` | `SELECT` | `resourceGroupName, subscriptionId` | Lists all RedisEnterprise clusters in a resource group. |
| `create` | `INSERT` | `clusterName, resourceGroupName, subscriptionId, data__sku` | Creates or updates an existing (overwrite/recreate, with potential downtime) cache cluster |
| `delete` | `DELETE` | `clusterName, resourceGroupName, subscriptionId` | Deletes a RedisEnterprise cache cluster. |
| `_list` | `EXEC` | `subscriptionId` | Gets all RedisEnterprise clusters in the specified subscription. |
| `_list_by_resource_group` | `EXEC` | `resourceGroupName, subscriptionId` | Lists all RedisEnterprise clusters in a resource group. |
| `update` | `EXEC` | `clusterName, resourceGroupName, subscriptionId` | Updates an existing RedisEnterprise cluster |
