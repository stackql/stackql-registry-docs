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
import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';

Creates, updates, deletes or gets a <code>network_performance_metric_subscription</code> resource or lists <code>network_performance_metric_subscriptions</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>network_performance_metric_subscriptions</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Resource Type definition for AWS::EC2::NetworkPerformanceMetricSubscription</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.ec2.network_performance_metric_subscriptions" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="source" /></td><td><code>string</code></td><td>The starting Region or Availability Zone for metric to subscribe to.</td></tr>
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
    <td><CopyableCode code="Source, Destination, Metric, Statistic, region" /></td>
  </tr>
  <tr>
    <td><CopyableCode code="delete_resource" /></td>
    <td><code>DELETE</code></td>
    <td><CopyableCode code="data__Identifier, region" /></td>
  </tr>
  <tr>
    <td><CopyableCode code="list_resource" /></td>
    <td><code>SELECT</code></td>
    <td><CopyableCode code="region" /></td>
  </tr>
  <tr>
    <td><CopyableCode code="get_resource" /></td>
    <td><code>SELECT</code></td>
    <td><CopyableCode code="data__Identifier, region" /></td>
  </tr>
</tbody></table>

## `SELECT` examples
List all <code>network_performance_metric_subscriptions</code> in a region.
```sql
SELECT
region,
source,
destination,
metric,
statistic
FROM aws.ec2.network_performance_metric_subscriptions
WHERE region = 'us-east-1';
```
Gets all properties from a <code>network_performance_metric_subscription</code>.
```sql
SELECT
region,
source,
destination,
metric,
statistic
FROM aws.ec2.network_performance_metric_subscriptions
WHERE region = 'us-east-1' AND data__Identifier = '<Source>|<Destination>|<Metric>|<Statistic>';
```


## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>network_performance_metric_subscription</code> resource, using [__`stack-deploy`__](https://pypi.org/project/stack-deploy/).

<Tabs
    defaultValue="required"
    values={[
      { label: 'Required Properties', value: 'required', },
      { label: 'All Properties', value: 'all', },
      { label: 'Manifest', value: 'manifest', },
    ]
}>
<TabItem value="required">

```sql
/*+ create */
INSERT INTO aws.ec2.network_performance_metric_subscriptions (
 Source,
 Destination,
 Metric,
 Statistic,
 region
)
SELECT 
'{{ Source }}',
 '{{ Destination }}',
 '{{ Metric }}',
 '{{ Statistic }}',
'{{ region }}';
```
</TabItem>
<TabItem value="all">

```sql
/*+ create */
INSERT INTO aws.ec2.network_performance_metric_subscriptions (
 Source,
 Destination,
 Metric,
 Statistic,
 region
)
SELECT 
 '{{ Source }}',
 '{{ Destination }}',
 '{{ Metric }}',
 '{{ Statistic }}',
 '{{ region }}';
```
</TabItem>
<TabItem value="manifest">

```yaml
version: 1
name: stack name
description: stack description
providers:
  - aws
globals:
  - name: region
    value: '{{ vars.AWS_REGION }}'
resources:
  - name: network_performance_metric_subscription
    props:
      - name: Source
        value: '{{ Source }}'
      - name: Destination
        value: '{{ Destination }}'
      - name: Metric
        value: '{{ Metric }}'
      - name: Statistic
        value: '{{ Statistic }}'

```
</TabItem>
</Tabs>

## `DELETE` example

```sql
/*+ delete */
DELETE FROM aws.ec2.network_performance_metric_subscriptions
WHERE data__Identifier = '<Source|Destination|Metric|Statistic>'
AND region = 'us-east-1';
```

## Permissions

To operate on the <code>network_performance_metric_subscriptions</code> resource, the following permissions are required:

### Create
```json
ec2:DescribeAwsNetworkPerformanceMetricSubscriptions,
ec2:EnableAwsNetworkPerformanceMetricSubscription
```

### Read
```json
ec2:DescribeAwsNetworkPerformanceMetricSubscriptions
```

### Delete
```json
ec2:DescribeAwsNetworkPerformanceMetricSubscriptions,
ec2:DisableAwsNetworkPerformanceMetricSubscription
```

### List
```json
ec2:DescribeAwsNetworkPerformanceMetricSubscriptions
```

