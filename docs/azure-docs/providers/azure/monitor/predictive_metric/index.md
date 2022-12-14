---
title: predictive_metric
hide_title: false
hide_table_of_contents: false
keywords:
  - predictive_metric
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
<tr><td><b>Name</b></td><td><code>predictive_metric</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.monitor.predictive_metric</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `targetResourceId` | `string` | resource of the predictive metric. |
| `timespan` | `string` | The timespan for which the data was retrieved. Its value consists of two datetimes concatenated, separated by '/'.  This may be adjusted in the future and returned back from what was originally requested. |
| `data` | `array` | the value of the collection. |
| `interval` | `string` | The interval (window size) for which the metric data was returned in.  This may be adjusted in the future and returned back from what was originally requested.  This is not present if a metadata request was made. |
| `metricName` | `string` | The metrics being queried |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| `PredictiveMetric_Get` | `SELECT` | `aggregation, autoscaleSettingName, resourceGroupName, subscriptionId` |
