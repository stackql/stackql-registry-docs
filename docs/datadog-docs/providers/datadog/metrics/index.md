---
title: metrics
hide_title: false
hide_table_of_contents: false
keywords:
  - metrics
  - datadog
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, monitor, and manage Datadog resources using SQL
custom_edit_url: null
image: /img/providers/datadog/stackql-datadog-provider-featured-image.png
---
The Metrics Endpoint Allows You To:

- Post Metrics Data So It Can Be Graphed On Datadog’S Dashboards
- Query Metrics From Any Time Period (Timeseries And Scalar)
- Modify Tag Configurations For Metrics
- View Tags And Volumes For Metrics

**Note**: A Graph Can Only Contain A Set Number Of Points
And As The Timeframe Over Which A Metric Is Viewed Increases,
Aggregation Between Points Occurs To Stay Below That Set Number.

The Post, Patch, And Delete `Manage Tags` API Methods Can Only Be Performed By
A User Who Has The `Manage Tags For Metrics` Permission.  
    
:::info Service Summary

<div class="row">
<div class="providerDocColumn">
<span>total resources:&nbsp;<b>9</b></span><br />
<span>total selectable resources:&nbsp;<b>7</b></span><br />
<span>total methods:&nbsp;<b>20</b></span><br />
</div>
</div>

:::

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>datadog.metrics</code></td></tr>
<tr><td><b>Type</b></td><td>Service</td></tr>
<tr><td><b>Title</b></td><td>Datadog API V2 Collection - Metrics</td></tr>
<tr><td><b>Description</b></td><td>The Metrics Endpoint Allows You To:<br /><br />- Post Metrics Data So It Can Be Graphed On Datadog’S Dashboards<br />- Query Metrics From Any Time Period (Timeseries And Scalar)<br />- Modify Tag Configurations For Metrics<br />- View Tags And Volumes For Metrics<br /><br />**Note**: A Graph Can Only Contain A Set Number Of Points<br />And As The Timeframe Over Which A Metric Is Viewed Increases,<br />Aggregation Between Points Occurs To Stay Below That Set Number.<br /><br />The Post, Patch, And Delete `Manage Tags` API Methods Can Only Be Performed By<br />A User Who Has The `Manage Tags For Metrics` Permission.</td></tr>
<tr><td><b>Id</b></td><td><code>metrics:v23.12.00194</code></td></tr>
</tbody></table>

## Resources
<div class="row">
<div class="providerDocColumn">
<a href="/providers/datadog/metrics/active_metric_configurations/">active_metric_configurations</a><br />
<a href="/providers/datadog/metrics/metrics/">metrics</a><br />
<a href="/providers/datadog/metrics/metrics_output_series/">metrics_output_series</a><br />
<a href="/providers/datadog/metrics/scalar_data/">scalar_data</a><br />
<a href="/providers/datadog/metrics/tag_configuration_by_name/">tag_configuration_by_name</a><br />
</div>
<div class="providerDocColumn">
<a href="/providers/datadog/metrics/tag_configurations/">tag_configurations</a><br />
<a href="/providers/datadog/metrics/tags_by_metric_names/">tags_by_metric_names</a><br />
<a href="/providers/datadog/metrics/timeseries_data/">timeseries_data</a><br />
<a href="/providers/datadog/metrics/volumes_by_metric_name/">volumes_by_metric_name</a><br />
</div>
</div>
