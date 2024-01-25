---
title: database_accounts_metric_definitions
hide_title: false
hide_table_of_contents: false
keywords:
  - database_accounts_metric_definitions
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
<tr><td><b>Name</b></td><td><code>database_accounts_metric_definitions</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.cosmos_db.database_accounts_metric_definitions</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `name` | `object` | A metric name. |
| `metricAvailabilities` | `array` | The list of metric availabilities for the account. |
| `primaryAggregationType` | `string` | The primary aggregation type of the metric. |
| `resourceUri` | `string` | The resource uri of the database. |
| `unit` | `string` | The unit of the metric. |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| `list` | `SELECT` | `accountName, resourceGroupName, subscriptionId` |
| `_list` | `EXEC` | `accountName, resourceGroupName, subscriptionId` |
