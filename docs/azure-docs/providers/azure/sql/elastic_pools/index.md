---
title: elastic_pools
hide_title: false
hide_table_of_contents: false
keywords:
  - elastic_pools
  - sql
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
<tr><td><b>Name</b></td><td><code>elastic_pools</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.sql.elastic_pools</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `kind` | `string` | Kind of elastic pool. This is metadata used for the Azure portal experience. |
| `location` | `string` | Resource location. |
| `properties` | `object` | Properties of an elastic pool |
| `sku` | `object` | An ARM Resource SKU. |
| `tags` | `object` | Resource tags. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `ElasticPools_Get` | `SELECT` | `elasticPoolName, resourceGroupName, serverName, subscriptionId` | Gets an elastic pool. |
| `ElasticPools_ListByServer` | `SELECT` | `resourceGroupName, serverName, subscriptionId` | Gets all elastic pools in a server. |
| `ElasticPools_CreateOrUpdate` | `INSERT` | `elasticPoolName, resourceGroupName, serverName, subscriptionId, data__location` | Creates or updates an elastic pool. |
| `ElasticPools_Delete` | `DELETE` | `elasticPoolName, resourceGroupName, serverName, subscriptionId` | Deletes an elastic pool. |
| `ElasticPools_Failover` | `EXEC` | `elasticPoolName, resourceGroupName, serverName, subscriptionId` | Failovers an elastic pool. |
| `ElasticPools_ListMetricDefinitions` | `EXEC` | `elasticPoolName, resourceGroupName, serverName, subscriptionId` | Returns elastic pool metric definitions. |
| `ElasticPools_ListMetrics` | `EXEC` | `$filter, elasticPoolName, resourceGroupName, serverName, subscriptionId` | Returns elastic pool  metrics. |
| `ElasticPools_Update` | `EXEC` | `elasticPoolName, resourceGroupName, serverName, subscriptionId` | Updates an elastic pool. |
