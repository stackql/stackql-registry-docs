---
title: throughput_pool
hide_title: false
hide_table_of_contents: false
keywords:
  - throughput_pool
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
<tr><td><b>Name</b></td><td><code>throughput_pool</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.cosmos_db.throughput_pool</code></td></tr>
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
| `get` | `SELECT` | `resourceGroupName, subscriptionId, throughputPoolName` | Retrieves the properties of an existing Azure Cosmos DB Throughput Pool |
| `create_or_update` | `INSERT` | `resourceGroupName, subscriptionId, throughputPoolName` | Creates or updates an Azure Cosmos DB ThroughputPool account. The "Update" method is preferred when performing updates on an account. |
| `delete` | `DELETE` | `resourceGroupName, subscriptionId, throughputPoolName` | Deletes an existing Azure Cosmos DB Throughput Pool. |
| `update` | `EXEC` | `resourceGroupName, subscriptionId, throughputPoolName` | Updates the properties of an existing Azure Cosmos DB Throughput Pool. |
