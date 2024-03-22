---
title: network_performance_metric_subscription
hide_title: false
hide_table_of_contents: false
keywords:
  - network_performance_metric_subscription
  - ec2
  - aws
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage AWS resources using SQL
custom_edit_url: null
image: /img/providers/aws/stackql-aws-provider-featured-image.png
---
Gets an individual <code>network_performance_metric_subscription</code> resource

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>network_performance_metric_subscription</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>network_performance_metric_subscription</td></tr>
<tr><td><b>Id</b></td><td><code>awscc.ec2.network_performance_metric_subscription</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>source</code></td><td><code>string</code></td><td>The starting Region or Availability Zone for metric to subscribe to.</td></tr>
<tr><td><code>destination</code></td><td><code>string</code></td><td>The target Region or Availability Zone for the metric to subscribe to.</td></tr>
<tr><td><code>metric</code></td><td><code>string</code></td><td>The metric type to subscribe to.</td></tr>
<tr><td><code>statistic</code></td><td><code>string</code></td><td>The statistic to subscribe to.</td></tr>
<tr><td><code>region</code></td><td><code>string</code></td><td>AWS region.</td></tr>

</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Example
```sql
SELECT
region,
source,
destination,
metric,
statistic
FROM awscc.ec2.network_performance_metric_subscription
WHERE data__Identifier = '<Source>|<Destination>|<Metric>|<Statistic>';
```

## Permissions

To operate on the <code>network_performance_metric_subscription</code> resource, the following permissions are required:

### Read
```json
ec2:DescribeAwsNetworkPerformanceMetricSubscriptions
```

### Delete
```json
ec2:DescribeAwsNetworkPerformanceMetricSubscriptions,
ec2:DisableAwsNetworkPerformanceMetricSubscription
```

