---
title: metrics_at_subscription_scope_post
hide_title: false
hide_table_of_contents: false
keywords:
  - metrics_at_subscription_scope_post
  - monitor
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
<tr><td><b>Name</b></td><td><code>metrics_at_subscription_scope_post</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.monitor.metrics_at_subscription_scope_post</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `cost` | `number` | The integer value representing the relative cost of the query. |
| `interval` | `string` | The interval (window size) for which the metric data was returned in ISO 8601 duration format with a special case for 'FULL' value that returns single datapoint for entire time span requested (*Examples: PT15M, PT1H, P1D, FULL*). <br />This may be adjusted and different from what was originally requested if AutoAdjustTimegrain=true is specified. This is not present if a metadata request was made. |
| `namespace` | `string` | The namespace of the metrics being queried |
| `resourceregion` | `string` | The region of the resource being queried for metrics. |
| `timespan` | `string` | The timespan for which the data was retrieved. Its value consists of two datetimes concatenated, separated by '/'.  This may be adjusted in the future and returned back from what was originally requested. |
| `value` | `array` | The value of the collection. |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| `list` | `SELECT` | `interval, metricName, region, subscriptionId, timespan` |
