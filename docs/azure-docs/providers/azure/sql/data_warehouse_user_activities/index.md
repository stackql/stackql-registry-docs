---
title: data_warehouse_user_activities
hide_title: false
hide_table_of_contents: false
keywords:
  - data_warehouse_user_activities
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
<tr><td><b>Name</b></td><td><code>data_warehouse_user_activities</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.sql.data_warehouse_user_activities</code></td></tr>
</tbody></table>

## Fields
`SELECT` not supported for this resource, use `SHOW METHODS` to view available operations for the resource and then invoke a supported method using the `EXEC` command  
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `DataWarehouseUserActivities_Get` | `SELECT` | `dataWarehouseUserActivityName, databaseName, resourceGroupName, serverName, subscriptionId` | Gets the user activities of a data warehouse which includes running and suspended queries |
| `DataWarehouseUserActivities_ListByDatabase` | `SELECT` | `databaseName, resourceGroupName, serverName, subscriptionId` | List the user activities of a data warehouse which includes running and suspended queries |
