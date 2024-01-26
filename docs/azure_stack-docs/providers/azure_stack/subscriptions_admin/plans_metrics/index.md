---
title: plans_metrics
hide_title: false
hide_table_of_contents: false
keywords:
  - plans_metrics
  - subscriptions_admin
  - azure_stack    
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
<tr><td><b>Name</b></td><td><code>plans_metrics</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure_stack.subscriptions_admin.plans_metrics</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `endTime` | `string` | End time of the metric. |
| `metricUnit` | `string` | The resource metric unit. |
| `metricValues` | `array` | List of metric values. |
| `startTime` | `string` | Start time of the metric. |
| `timeGrain` | `string` | Timespan of the metric. |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| `list` | `SELECT` | `plan, resourceGroupName, subscriptionId` |
| `_list` | `EXEC` | `plan, resourceGroupName, subscriptionId` |
