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
| `get` | `SELECT` | `elasticPoolName, resourceGroupName, serverName, subscriptionId` | Gets an elastic pool. |
| `list_by_server` | `SELECT` | `resourceGroupName, serverName, subscriptionId` | Gets all elastic pools in a server. |
| `create_or_update` | `INSERT` | `elasticPoolName, resourceGroupName, serverName, subscriptionId, data__location` | Creates or updates an elastic pool. |
| `delete` | `DELETE` | `elasticPoolName, resourceGroupName, serverName, subscriptionId` | Deletes an elastic pool. |
| `_list_by_server` | `EXEC` | `resourceGroupName, serverName, subscriptionId` | Gets all elastic pools in a server. |
| `failover` | `EXEC` | `elasticPoolName, resourceGroupName, serverName, subscriptionId` | Failovers an elastic pool. |
| `update` | `EXEC` | `elasticPoolName, resourceGroupName, serverName, subscriptionId` | Updates an elastic pool. |
