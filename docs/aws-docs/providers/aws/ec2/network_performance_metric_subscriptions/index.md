---
title: network_performance_metric_subscriptions
hide_title: false
hide_table_of_contents: false
keywords:
  - network_performance_metric_subscriptions
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

import CopyableCode from '@site/src/components/CopyableCode/CopyableCode';

Used to retrieve a list of <code>network_performance_metric_subscriptions</code> in a region or create a <code>network_performance_metric_subscriptions</code> resource, use <code>network_performance_metric_subscription</code> to operate on an individual resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>network_performance_metric_subscriptions</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Resource Type definition for AWS::EC2::NetworkPerformanceMetricSubscription</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.ec2.network_performance_metric_subscriptions" /></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><CopyableCode code="source" /></td><td><code>string</code></td><td>The starting Region or Availability Zone for metric to subscribe to.</td></tr>
<tr><td><CopyableCode code="destination" /></td><td><code>string</code></td><td>The target Region or Availability Zone for the metric to subscribe to.</td></tr>
<tr><td><CopyableCode code="metric" /></td><td><code>string</code></td><td>The metric type to subscribe to.</td></tr>
<tr><td><CopyableCode code="statistic" /></td><td><code>string</code></td><td>The statistic to subscribe to.</td></tr>
<tr><td><CopyableCode code="region" /></td><td><code>string</code></td><td>AWS region.</td></tr>

</tbody></table>

## Methods

<table><tbody>
  <tr>
    <th>Name</th>
    <th>Accessible by</th>
    <th>Required Params</th>
  </tr>
  <tr>
    <td><CopyableCode code="create_resource" /></td>
    <td><code>INSERT</code></td>
    <td><CopyableCode code="data__DesiredState, region" /></td>
  </tr>
  <tr>
    <td><CopyableCode code="list_resource" /></td>
    <td><code>SELECT</code></td>
    <td><CopyableCode code="region" /></td>
  </tr>
</tbody></table>

## `SELECT` Example
```sql
SELECT
region,
source,
destination,
metric,
statistic
FROM aws.ec2.network_performance_metric_subscriptions
WHERE region = 'us-east-1'
```

## Permissions

To operate on the <code>network_performance_metric_subscriptions</code> resource, the following permissions are required:

### Create
```json
ec2:DescribeAwsNetworkPerformanceMetricSubscriptions,
ec2:EnableAwsNetworkPerformanceMetricSubscription
```

### List
```json
ec2:DescribeAwsNetworkPerformanceMetricSubscriptions
```

