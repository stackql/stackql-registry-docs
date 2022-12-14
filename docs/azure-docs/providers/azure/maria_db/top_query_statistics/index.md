---
title: top_query_statistics
hide_title: false
hide_table_of_contents: false
keywords:
  - top_query_statistics
  - maria_db
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
<tr><td><b>Name</b></td><td><code>top_query_statistics</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.maria_db.top_query_statistics</code></td></tr>
</tbody></table>

## Fields
`SELECT` not supported for this resource, use `SHOW METHODS` to view available operations for the resource and then invoke a supported method using the `EXEC` command  
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `TopQueryStatistics_Get` | `SELECT` | `queryStatisticId, resourceGroupName, serverName, subscriptionId` | Retrieve the query statistic for specified identifier. |
| `TopQueryStatistics_ListByServer` | `SELECT` | `resourceGroupName, serverName, subscriptionId, data__properties` | Retrieve the Query-Store top queries for specified metric and aggregation. |
