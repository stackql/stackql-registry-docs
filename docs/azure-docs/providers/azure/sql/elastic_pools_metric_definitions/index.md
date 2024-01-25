---
title: elastic_pools_metric_definitions
hide_title: false
hide_table_of_contents: false
keywords:
  - elastic_pools_metric_definitions
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
<tr><td><b>Name</b></td><td><code>elastic_pools_metric_definitions</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.sql.elastic_pools_metric_definitions</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `name` | `object` | A database metric name. |
| `metricAvailabilities` | `array` | The list of database metric availabilities for the metric. |
| `primaryAggregationType` | `string` | The primary aggregation type defining how metric values are displayed. |
| `resourceUri` | `string` | The resource uri of the database. |
| `unit` | `string` | The unit of the metric. |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| `list` | `SELECT` | `elasticPoolName, resourceGroupName, serverName, subscriptionId` |
| `_list` | `EXEC` | `elasticPoolName, resourceGroupName, serverName, subscriptionId` |
