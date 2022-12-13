---
title: restorable_dropped_sql_pools
hide_title: false
hide_table_of_contents: false
keywords:
  - restorable_dropped_sql_pools
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
<tr><td><b>Name</b></td><td><code>restorable_dropped_sql_pools</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.synapse.restorable_dropped_sql_pools</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `location` | `string` | The geo-location where the resource lives |
| `properties` | `object` | The properties of a restorable dropped Sql pool |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `RestorableDroppedSqlPools_Get` | `SELECT` | `resourceGroupName, restorableDroppedSqlPoolId, subscriptionId, workspaceName` | Gets a deleted sql pool that can be restored |
| `RestorableDroppedSqlPools_ListByWorkspace` | `SELECT` | `resourceGroupName, subscriptionId, workspaceName` | Gets a list of deleted Sql pools that can be restored |
