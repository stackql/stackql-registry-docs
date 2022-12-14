---
title: big_data_pools
hide_title: false
hide_table_of_contents: false
keywords:
  - big_data_pools
  - synapse
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
<tr><td><b>Name</b></td><td><code>big_data_pools</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.synapse.big_data_pools</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `tags` | `object` | Resource tags. |
| `location` | `string` | The geo-location where the resource lives |
| `properties` | `object` | Properties of a Big Data pool powered by Apache Spark |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `BigDataPools_Get` | `SELECT` | `bigDataPoolName, resourceGroupName, subscriptionId, workspaceName` | Get a Big Data pool. |
| `BigDataPools_ListByWorkspace` | `SELECT` | `resourceGroupName, subscriptionId, workspaceName` | List Big Data pools in a workspace. |
| `BigDataPools_CreateOrUpdate` | `INSERT` | `bigDataPoolName, resourceGroupName, subscriptionId, workspaceName` | Create a new Big Data pool. |
| `BigDataPools_Delete` | `DELETE` | `bigDataPoolName, resourceGroupName, subscriptionId, workspaceName` | Delete a Big Data pool from the workspace. |
| `BigDataPools_Update` | `EXEC` | `bigDataPoolName, resourceGroupName, subscriptionId, workspaceName` | Patch a Big Data pool. |
