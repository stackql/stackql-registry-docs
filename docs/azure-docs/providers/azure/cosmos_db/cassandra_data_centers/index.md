---
title: cassandra_data_centers
hide_title: false
hide_table_of_contents: false
keywords:
  - cassandra_data_centers
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
<tr><td><b>Name</b></td><td><code>cassandra_data_centers</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.cosmos_db.cassandra_data_centers</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | The unique resource identifier of the database account. |
| `name` | `string` | The name of the database account. |
| `properties` | `object` | Properties of a managed Cassandra data center. |
| `type` | `string` | The type of Azure resource. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `clusterName, dataCenterName, resourceGroupName, subscriptionId` | Get the properties of a managed Cassandra data center. |
| `list` | `SELECT` | `clusterName, resourceGroupName, subscriptionId` | List all data centers in a particular managed Cassandra cluster. |
| `delete` | `DELETE` | `clusterName, dataCenterName, resourceGroupName, subscriptionId` | Delete a managed Cassandra data center. |
| `_list` | `EXEC` | `clusterName, resourceGroupName, subscriptionId` | List all data centers in a particular managed Cassandra cluster. |
| `create_update` | `EXEC` | `clusterName, dataCenterName, resourceGroupName, subscriptionId` | Create or update a managed Cassandra data center. When updating, overwrite all properties. To update only some properties, use PATCH. |
| `update` | `EXEC` | `clusterName, dataCenterName, resourceGroupName, subscriptionId` | Update some of the properties of a managed Cassandra data center. |
