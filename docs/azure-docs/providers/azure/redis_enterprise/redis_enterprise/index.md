---
title: redis_enterprise
hide_title: false
hide_table_of_contents: false
keywords:
  - redis_enterprise
  - redis_enterprise
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
<tr><td><b>Name</b></td><td><code>redis_enterprise</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.redis_enterprise.redis_enterprise</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `tags` | `object` | Resource tags. |
| `zones` | `array` | The Availability Zones where this cluster will be deployed. |
| `location` | `string` | The geo-location where the resource lives |
| `properties` | `object` | Properties of RedisEnterprise clusters, as opposed to general resource properties like location, tags |
| `sku` | `object` | SKU parameters supplied to the create RedisEnterprise operation. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `RedisEnterprise_Get` | `SELECT` | `clusterName, resourceGroupName, subscriptionId` | Gets information about a RedisEnterprise cluster |
| `RedisEnterprise_List` | `SELECT` | `subscriptionId` | Gets all RedisEnterprise clusters in the specified subscription. |
| `RedisEnterprise_ListByResourceGroup` | `SELECT` | `resourceGroupName, subscriptionId` | Lists all RedisEnterprise clusters in a resource group. |
| `RedisEnterprise_Create` | `INSERT` | `clusterName, resourceGroupName, subscriptionId, data__sku` | Creates or updates an existing (overwrite/recreate, with potential downtime) cache cluster |
| `RedisEnterprise_Delete` | `DELETE` | `clusterName, resourceGroupName, subscriptionId` | Deletes a RedisEnterprise cache cluster. |
| `RedisEnterprise_Update` | `EXEC` | `clusterName, resourceGroupName, subscriptionId` | Updates an existing RedisEnterprise cluster |
