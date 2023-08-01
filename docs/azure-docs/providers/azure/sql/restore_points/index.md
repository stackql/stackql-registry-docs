---
title: restore_points
hide_title: false
hide_table_of_contents: false
keywords:
  - restore_points
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
<tr><td><b>Name</b></td><td><code>restore_points</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.sql.restore_points</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `properties` | `object` | Properties of a database restore point |
| `location` | `string` | Resource location. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `RestorePoints_Get` | `SELECT` | `databaseName, resourceGroupName, restorePointName, serverName, subscriptionId` | Gets a restore point. |
| `RestorePoints_ListByDatabase` | `SELECT` | `databaseName, resourceGroupName, serverName, subscriptionId` | Gets a list of database restore points. |
| `RestorePoints_Create` | `INSERT` | `databaseName, resourceGroupName, serverName, subscriptionId, data__restorePointLabel` | Creates a restore point for a data warehouse. |
| `RestorePoints_Delete` | `DELETE` | `databaseName, resourceGroupName, restorePointName, serverName, subscriptionId` | Deletes a restore point. |
