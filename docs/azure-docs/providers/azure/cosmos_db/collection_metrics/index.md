---
title: collection_metrics
hide_title: false
hide_table_of_contents: false
keywords:
  - collection_metrics
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
<tr><td><b>Name</b></td><td><code>collection_metrics</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.cosmos_db.collection_metrics</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `name` | `object` | A metric name. |
| `endTime` | `string` | The end time for the metric (ISO-8601 format). |
| `metricValues` | `array` | The metric values for the specified time window and timestep. |
| `startTime` | `string` | The start time for the metric (ISO-8601 format). |
| `timeGrain` | `string` | The time grain to be used to summarize the metric values. |
| `unit` | `string` | The unit of the metric. |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| `list` | `SELECT` | `$filter, accountName, collectionRid, databaseRid, resourceGroupName, subscriptionId` |
| `_list` | `EXEC` | `$filter, accountName, collectionRid, databaseRid, resourceGroupName, subscriptionId` |
