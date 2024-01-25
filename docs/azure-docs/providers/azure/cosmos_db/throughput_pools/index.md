---
title: throughput_pools
hide_title: false
hide_table_of_contents: false
keywords:
  - throughput_pools
  - cosmos_db
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
<tr><td><b>Name</b></td><td><code>throughput_pools</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.cosmos_db.throughput_pools</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `location` | `string` | The geo-location where the resource lives |
| `properties` | `object` | Properties to update Azure Cosmos DB throughput pool. |
| `tags` | `object` | Resource tags. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `list` | `SELECT` | `subscriptionId` | Lists all the Azure Cosmos DB Throughput Pools available under the subscription. |
| `list_by_resource_group` | `SELECT` | `resourceGroupName, subscriptionId` | List all the ThroughputPools in a given resource group. |
| `_list` | `EXEC` | `subscriptionId` | Lists all the Azure Cosmos DB Throughput Pools available under the subscription. |
| `_list_by_resource_group` | `EXEC` | `resourceGroupName, subscriptionId` | List all the ThroughputPools in a given resource group. |
