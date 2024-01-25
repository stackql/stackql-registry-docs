---
title: throughput_pool_accounts
hide_title: false
hide_table_of_contents: false
keywords:
  - throughput_pool_accounts
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
<tr><td><b>Name</b></td><td><code>throughput_pool_accounts</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.cosmos_db.throughput_pool_accounts</code></td></tr>
</tbody></table>

## Fields
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `resourceGroupName, subscriptionId, throughputPoolAccountName, throughputPoolName` | Retrieves the properties of an existing Azure Cosmos DB Throughput Pool |
| `list` | `SELECT` | `resourceGroupName, subscriptionId, throughputPoolName` | Lists all the Azure Cosmos DB accounts available under the subscription. |
| `create` | `INSERT` | `resourceGroupName, subscriptionId, throughputPoolAccountName, throughputPoolName` | Creates or updates an Azure Cosmos DB ThroughputPool account. The "Update" method is preferred when performing updates on an account. |
| `delete` | `DELETE` | `resourceGroupName, subscriptionId, throughputPoolAccountName, throughputPoolName` | Removes an existing Azure Cosmos DB database account from a throughput pool. |
| `_list` | `EXEC` | `resourceGroupName, subscriptionId, throughputPoolName` | Lists all the Azure Cosmos DB accounts available under the subscription. |
